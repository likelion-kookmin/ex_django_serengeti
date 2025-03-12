# Django Serengeti 예제

## Contents

### 프로젝트 시작!

- [django 프로젝트 시작하기](https://github.com/likelion-kookmin/ex_django_serengeti/commit/e19d2dac564a1c08a2ef3a3e3db6b13e2ee048bb)
  - django는 프로젝트 시작 명령어를 제공합니다.
  - 원하는 디렉토리(위치)에서 `django-admin startproject ex_django_serengeti` 를 수행합니다.
- [.gitignore 파일 추가하기](https://github.com/likelion-kookmin/ex_django_serengeti/commit/0ddb6762f2580de8c3cef25ede49ba59513442bd) 
  - .gitignore 파일은 중요합니다. github에 파일을 올리는 상황이라면 항상 신경써야 합니다.
  - 이를 도와주는 [서비스](https://gitignore.io/)가 있습니다.
  - django, python, venv, vscode, pycharm 등의 사용할 것을 추가하고 파일을 만들어봅시다.
- [가상환경 설정하기](https://github.com/likelion-kookmin/ex_django_serengeti/commit/d9f694f68c9466a3681e07d5e10377d5d4c8e822)
  - 가상환경은 각 프로젝트마다 달라지는 패키지 목록들을 쉽게 관리할 수 있게 해줍니다.
  - 하지만, 협업을 한다면 어떤 패키지를 쓰고 있는 프로젝트인지 명시해야겠죠?
  - requirements.txt를 통해 일단 관리해봅시다. 이후에는 다른 패키지 관리자를 사용해봅시다!

### Ping Pong 앱을 통한 django Overview

- [ping_pong 앱 만들기](http://github.com/likelion-kookmin/ex_django_serengeti/commit/0caf3b8bf4ece318ecfcd5a26e8488c7e0113247)
  - django는 app 단위로 서비스를 나눕니다.
  - 이때, app을 만드는 명령어도 제공합니다.
  - `python manage.py startapp ping_pong`를 수행해봅시다.
- [ping pong 기능 만들기](https://github.com/likelion-kookmin/ex_django_serengeti/commit/43a95e29ce51c25c8e24512a4d1b69179da79f86)
  - urls.py를 간단하게 확인해봅시다.
  - views 파일과 templates 폴더에 대해 알아봅시다.
- [name을 쿼리 파라미터로 받고, 다시 보여주기](https://github.com/likelion-kookmin/ex_django_serengeti/commit/6ab65ef77d8503920175d672a5399d09ef992ff2)
  - name이라는 파라미터를 받고, 다시 템플릿에 노출시켜봅시다.

### 모델에 대해

- Django의 기본 User 모델을 활용하면서 회원가입/로그인/로그아웃 구성해보기
  - [관련 기능을 수행할 간단한 account app 생성](https://github.com/likelion-kookmin/ex_django_serengeti/commit/4169fd207bd4555051479260f4c6d1fb164f5bf4) 
  - [회원가입/로그인/로그아웃을 확인하기 위한 main app 생성](https://github.com/likelion-kookmin/ex_django_serengeti/commit/bf80014333ed18cde903703815fdefb115243d57)
  - [메인 페이지에 대한 url, view, template 추가](https://github.com/likelion-kookmin/ex_django_serengeti/commit/db799624e95ce5d86c911bbfe7f7095a4da6a282)
  - [django 기본 auth user 모델을 활용한 로그인 / 회원가입 기능 추가](https://github.com/likelion-kookmin/ex_django_serengeti/commit/15a785ab58f43ebaa445b7687f323dde0627e983)
  - [메인 페이지에서 로그인상태에 따른 메뉴를 구분해보기](https://github.com/likelion-kookmin/ex_django_serengeti/commit/6ca06ce5d75110e4e2cf1e4fa329ece68d44cfa5)
- [Article 모델을 만들어봅시다.]()
- [Comment 모델을 만들어봅시다.]()
- [(모델 응용) ping pong 호출 기록을 남겨봅시다]()
- [(모델 응용) 대댓글 기능을 만들어봅시다.]()


### 게시글과 댓글 View와 Template 구성하기


### 게시글에 이미지를 첨부해보자


### CSS 파일을 추가하고 사이트를 꾸며보자


### 간단한 텍스트 에디터도 추가해보자.


### 과제
