from livereload import Server, shell

server = Server()
server.watch("./exercises/*.py",
             shell("python3 run_all_tests.py --quiet"), delay=3)
server.serve(port=8080, host="localhost",
             root="./reports/test_results.html")
