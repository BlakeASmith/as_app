# as_app
Open websites in Chromium's app mode.

## Motivation

I use several GSuite apps such as Google Sheets and Google Docs, but there are not suitible 
linux clients available for these apps. Running them in [app](https://superuser.com/questions/33548/starting-google-chrome-in-application-mode) mode using the `--app` CLI option
is a good substitute for this. 

## Installation

```shell script
git clone https://github.com/BlakeASmith/as_app.git
pip install . 
```

## Usage

Launch a website in it's own window, without any borders or browser options. 

```shell script
asapp https://duckduckgo.com
```
