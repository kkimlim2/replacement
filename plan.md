## 0. 데이터 
### 0.1 분석 전 EDA:
i) missing 값이 있는지?  
ii) 변수들의 분포(1차원적)  
iii) 변수들 간 correlation  
iv) 또 있을지 생각해보자..  

#### data set(bankrupt) 이용하려고 했으나 col이 너무 많아서 일단 보류  

#### 데이터 셋 방향: 
i) 작은 데이터셋, numerical만  
ii) 작은 데이터셋, time series, numerical만  
iii) 작은 데이터셋, categorical, numerical  
iv) 작은 데이터셋, time series, categorical, numerical    
v) 큰 데이터 셋  
쭉..  

###########################  
## ## 1. 브레인스토밍 ## ##  
###########################    
  
## 결측치가 없는 데이터 셋에서 결측치를 만들어내고, 결과값 비교  
### 1.1 시도해볼 variation  
i) col의 수 (1->2->4..)  
ii) 결측치의 수 (10%->30%->50%, 근데 솔직히 50%면 col 자체를 버리는 게 나을 것 같은데)  
iii) col의 종류(1번 행, 2번 행 등) #근데 이 data set에는 categorical이 없으니까 다른 데이터 셋으로도 해볼 것 
iv) 

### 1.2 잘 대체되였는지 확인할 방법: 전체적인 분석이 달라졌는지 중점으로 확인  
i) 대푯값 비교: 기본적인 대푯값(mean,median, mode, variance)  
ii) 시각적 비교: kde 함수
iii) MSE를 비교해보고 싶은데 그건 어떻게 할 수 있지? 

### 1.3 어떤 방법을 써서 대체할 것인가
####  1.3.1 clustering을 사용하는 것에 대한 의문들..
clustering은 missing value를 대체한 다음에 이용가능함  
categorical한 변수들을 포함하면 문제가 생길 가능성(왜냐하면 유클리드 거리를 쓰기 때문)  
그리고 high dimension에서는 시간이 오래 걸릴듯 (이건 이미 dbscan에서 본 문제)  
parameter은 어떻게 정할 것인가  

#### 1.3.2 그래서 대신 사용할 수 있는 방법들을 생각해보자 -한계: CLUSTERING WITH MISSING VALUE에 관한 논문이 없음... 
1. 결측치 있는 col을 제외하고 clustering을 해보자! <- 그렇지만 그런 col이 많아진다면 대처가 불가능해질 듯  
2. 
    - 일단 먼저 단일 대체(mean,mode) + missing indicator 칼럼을 넣음(그런데 이게 칼럼이 많아지면 어떻게 넣을지도 고민해봐야 함)
    - clustering을 돌리고 
    - 대체했던 것들 drop 시키고 그 다음에 group을 봐서 대체하는 것
3. 통조입에서 배웠던 hot deck 대체 (근데 이건 clustering은 아님)
4. KNNIMPUTER  
  
5. 회귀곡선
6. 상관도

#### 1.3.3 1차 시도: stochastic regression  
왜냐하면 전문적 지식이 있는 사람들이라면 굳이 이 플랫폼을 쓸 필요가 있을까? 하는 의문이 들었음
그렇기에 일단 간단하게 하려고 함  
- 일단 missing value을 기존의 값들 중에서 random하게 뽑아서 impute함 
- missing value가 있는 col에 대해서 각각 regression model을 적용함 (y가 돌아가면서 바뀜)
- 완성  
    근데 문제는 어떻게 검정하지? 이 regression model에 대해서 좀 알아보고 싶은데.. 이를테면 adjusted r 이 어떤 상탠지 보고 싶달까
https://www.kaggle.com/shashankasubrahmanya/missing-data-imputation-using-regression  
- 근데 이럴꺼면 똑같이 dbscan에도 써도 되잖아?! 놀라운 깨달음..
