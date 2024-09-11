import time


class User:
    def __init__(self, nickname: str, password, age: int):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return self.nickname


class Video:
    def __init__(self, title: str, duration: int, time_mow=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_mow
        self.adult_mode = adult_mode


class UrTube:
    users = []
    videos = []

    def __init__(self):
        self.current_user = None

    def log_in(self, nickname, password):
        for user in UrTube.users:
            if user.nickname == nickname and user.password == hash(password):
                self.current_user = user
                print(f'Вход для пользователя {nickname} успешно выполнен')
                break
            else:
                print('Неверные учетные данные. Пожалуйста, повторите попытку')

    def register(self, nickname: str, password, age: int):
        for user in UrTube.users:
            if user.nickname == nickname:
                print(f'Пользователь {nickname} уже существует')
                return
        nickname = User(nickname, password, age)
        UrTube.users.append(nickname)
        print(f'Регистрация пользователя {nickname.nickname} успешно выполнена')
        self.current_user = nickname
        print(f'Вход под пользователем {nickname.nickname} успешно выполнен')

    def log_out(self):
        current_user = self.current_user
        self.current_user = None
        print(f'Выход пользователя {current_user} успешно выполнен')

    def add(self, *args: Video):
        for video in args:
            if video in UrTube.videos:
                print(f'Видеоролик "{video.title}" уже существует. Пропущен')
                continue
            UrTube.videos.append(video)
            print(f'Видеоролик "{video.title}" успешно загружен')

    def get_videos(self, input_search: str):
        videos_found = []
        for video in UrTube.videos:
            if input_search.lower() in video.title.lower():
                videos_found.append(video.title)
        return videos_found


    def watch_video(self, video_title):
        if not self.current_user:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return
        for video in UrTube.videos:
            if video.title == video_title:
                if video.adult_mode:
                    if self.current_user.age < 18:
                        print('Вам нет 18 лет, пожалуйста покиньте страницу')
                        return
                for second in range(video.time_now, video.duration):
                    video.time_now += 1
                    print(video.time_now, end=' ')
                    time.sleep(1)
                print('Конец видео')
                video.time_now = 0


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')