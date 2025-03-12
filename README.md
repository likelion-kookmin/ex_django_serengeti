# Django Serengeti 예제

> 해당 예제에서는 Django 커뮤니티 사이트 예제를 다룹니다.

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
- Article 모델을 만들어봅시다.
  - [article 앱 생성](https://github.com/likelion-kookmin/ex_django_serengeti/commit/ba3fa1d02345ca50d542380f6d2a6a50bf06052b)
  - [Article 모델 추가 및 마이그레이션 파일 생성](https://github.com/likelion-kookmin/ex_django_serengeti/commit/f5f3542cfc5757098ddc0a7f38aa17dc45a7cabf)
  - [Admin에서 Article 모델 확인해보기](https://github.com/likelion-kookmin/ex_django_serengeti/commit/8b0b70b1484d016cda0b0b3fe9f9f2cc530bca68)
- Comment 모델을 만들어봅시다.
  - [Comment 모델 추가 및 마이그레이션 파일 생성](https://github.com/likelion-kookmin/ex_django_serengeti/commit/afcab931349724615de855c7b8a4388170b4a89b)
  - [Admin에서 Comment 모델 확인해보기](https://github.com/likelion-kookmin/ex_django_serengeti/commit/9d42478cd9c5779f6a72b2b4b8e3859a68645f8d)

### 게시글과 댓글 View와 Template 구성하기

- [게시글 관련 url과 views를 먼저 정의해보자](https://github.com/likelion-kookmin/ex_django_serengeti/commit/411626c099047f2d4be71706a265378b7eb81b26)
- [게시글 조회 페이지를 만들어보자](https://github.com/likelion-kookmin/ex_django_serengeti/commit/30f6097098a2a583d5328e2b9116b60922384978)
- [게시글 목록 페이지를 만들어보자](https://github.com/likelion-kookmin/ex_django_serengeti/commit/08a26d1a2c99766a77061bc0293db0acf2d3508f)
- [게시글 생성 페이지를 만들어보자](https://github.com/likelion-kookmin/ex_django_serengeti/commit/0af32ac8c2a28b30fa3769293294e39cfc0328d9)
- [게시글 수정 페이지를 만들어보자](http://github.com/likelion-kookmin/ex_django_serengeti/commit/e660c310e8b4d7989a1f9828de78c2198b8bb332)
- [게시글에 댓글 목록이 보이도록 해보자](https://github.com/likelion-kookmin/ex_django_serengeti/commit/c3d2dbb4ee41bbf76d6ef5a329aa890006cf98c9)
- [게시글에 댓글을 달 수 있도록 해보자](https://github.com/likelion-kookmin/ex_django_serengeti/commit/e9d3641b52c80360087f0af2e0ae7da45e9af39b)
- [(응용) edit, update와 같이 꼭 2개의 view가 있어야할까?](https://github.com/likelion-kookmin/ex_django_serengeti/commit/bf20e9543ea6e2f1a1ab4953cfd3643d464e656e)
- [(응용) 내가 작성한 글만 수정/삭제할 수 있게 제한해보자](https://github.com/likelion-kookmin/ex_django_serengeti/commit/a6c0e01336e9299fe1a948c40c84368428158d5b)

### 게시글에 이미지를 첨부해보자

- [이미지를 첨부하기 위한 media 설정 추가](https://github.com/likelion-kookmin/ex_django_serengeti/commit/27865d5f3242a01f7b2da9012ec626bcec9e6d47)
- [Article 모델에 image 필드 추가하기](https://github.com/likelion-kookmin/ex_django_serengeti/commit/208fd2e5286d78a9ab8f640658e2c2903bf1849c)
- [게시글 페이지에 반영하기](https://github.com/likelion-kookmin/ex_django_serengeti/commit/9329eb9c1340b1fe066f0cc0dc3715e181713001)

### CSS 파일을 추가하고 사이트를 꾸며보자

- [navigation 등의 레이아웃을 쉽게 활용하기 위한 템플릿 상속]()
- [CSS 파일 추가하여 사이트 꾸며보기]()

### 응용
- [(모델 응용) ping pong 호출 기록을 남겨봅시다]()
- [(모델 응용) 대댓글 기능을 만들어봅시다.]()
- [간단한 텍스트 에디터도 추가해보자.]()
- [(패키지 적용) 예쁜 어드민을 사용해보기]()

### 과제
- 댓글 수정 기능
- 더 예쁜 UI
- 메인 페이지 구성
- 401, 403, 404, 500 http status code 등에 대한 화면을 구성해보기
