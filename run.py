from proj.main import app


if __name__ == '__main__':
    app.start(["worker", "-B", "-l", "INFO"])