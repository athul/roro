- Program for q1 can be found in the `/prog` folder
- Program for search can be found in the `/api` folder

## Running the API
Clone the repo then
```bash
$ cd api/
$ pipenv install
$ FLASK_APP=app.py FLASK_ENV=development flask run
```
## Running the program
```bash
$ cd prog
$ go run main.go twain.txt
# OR
$ go build main.go
$ ./main twain.txt
```