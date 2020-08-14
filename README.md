# DontBuyJustAdoptProject
유기동물 입양률 예측모델 using Machine learning & Deep learning
1. 개요   
1-1. 분석배경   
유기동물 문제가 공론화 되면서, 유기동물 입양에 대한 관심이 많아졌다. 이에 대응하여 유기동물의 특성에 따라 입양률을 예측해보고 입양률이 낮다고 예측되는 동물부터 부정적인 특성을 개선하여 입양률을 높이고자 한다.   
1-2. 가설   
유기동물의 나이와 특성에 따라 입양률이 다를 것이다.   
따라서, 부정적인 특성을 개선한다면 입양률이 올라갈 것이다.   

1-2. 진행방향   

2. 구현과정   
2-1. 서비스 아키텍쳐    
동물보호관리시스템(via 공공데이터포털) --> 크롤링, 스케줄링 --->sqlite3, mysql  ----> python(preprocessing, machine learning, deep learning) ---> Django(web service)    
   
2-2. 구현기술    
머신러닝 모델, 딥러닝(tensorflow perceptron model)   

3. 진행과정   
       3-1.데이터 수집: 공공데이터 포털에서 공고를 크롤링 하여 sqlite, mariadb(mysql) 에 데이터베이스화     
       3-2.전처리: 일정한 형식 없이 적힌 각 동물의 특성을 담은 feature 컬럼을 텍스트마이닝하여 질병, 부상, 장애여부, 성격, 생후 3개월 이내 여부 특성으로 원-핫 인코딩을 통해 범주화함.      
       3-3.분석: 동물종류, 나이, 성별, 무게, 종(species)m 특징을 독립변수로, 공고마감결과(자연사, 안락사/ 입양,기증) 을 종속변수로하여 binary result predict      
       logistic regression, random forest regression, perceptron model 등을 통해 분석 진행. 평균적으로약 70% 의 정확도를 기록하는 모델 생성.    
       3-4.서비스: django에서 각 독립변수에 해당하는 값을 입력하면 입양률을 예측해주는 웹 서비스 생성.    
 

4. 결론 및 확장    
4-1. 가설검증    
나이와 특성에 따라 입양률이 달라지는 것 확인. 

4-2. 확장방향      
예측모델을 활용한 유기동물 입양 추천 시스템      
github for project     
