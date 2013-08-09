# OARS Tests

## Local Installation
Follow these steps to get up and running in your local environment
Everything below assumes you're working on Mac

1. Clone into the repository.
```
$ git clone git@github.com:2tor/oars-tests.git
```

2. Download and install the following dependencies
```
$ sudo apt-get install python-pip
$ sudo easy_install selenium
$ sudo easy_install faker
```

3. Ensure the chromedriver server is installed in ./oars-tests/src/resources. If not then it can be downloaded from https://code.google.com/p/chromedriver/downloads/list.


## TestRunner Commands

| --set Parameters   | Alternate  | Required  | Default   | Description                      |
| -----------------  | ---------  | --------- | --------- | -------------------------------- |
| `test`             | -T         | yes       | None      | Specifies which test to execute  |
| `driver`           | -D         | yes       | None      | Specifies which browser to run   |
| `url`              | -U         | yes       | None      | The URL to OARS in test          | 

#### Example
Navigate to root:

    $ python testRunner.py -T 'testPersonalInfo' -P 'au-mir' -U https://au-mir-oars-sb01-qa.2u.com/

