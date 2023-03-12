# AES_sample2

## 디렉토리 구조
```
AES_sample2  
    - templates  
        - emp01.html  
    - app.py   
    - create_table.py  
    - dao.py  
    - delete_data.py  
    - insert_data.py  
    - list.py  
    - select_data.py  
```  

- app.py : 플라스크 서버 실행 파일  
- create_table.py : 데이터베이스 테이블 생성 파일  
- dao.py : 유일하게 데이터베이스 접근 정보를 가지고 접근하는 파일  
- delete_data.py : 데이터 삭제 파일  
- insert_data.py : 데이터 삽입 파일  
- list.py : 회원 목록을 리스트 형태로 반환하는 파일  
- select_data.py : 테이블 데이터 조회 파일  
- test.py : 암호화/복호화 함수 정의 파일

## 코드 적용 방법
1. Flask 서버 열기
```python
> python app.py
```
2. db 테이블 생성
```python
> python create_table.py
```
3. 데이터 insert
```python
> python insert_data.py
```
4. 데이터 확인
```python
> python select_data.py
```  
5. 데이터 delete
```python
> python delete_data.py
```  
6. 전체적으로 접근
```python
> python dao.py
```