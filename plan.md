## 0. 데이터 분석
### 점검해볼 사항:
i) missing 값이 있는지?  
ii) 변수들의 분포(1차원적)  
iii) 변수들 간 correlation  
iv) 또 있을지 생각해보자..  

#### data set(bankrupt) 이용하려고 했으나 col이 너무 많아서 일단 보류  

#### 그래서...
i) 작은 데이터셋, numerical만  
ii) 작은 데이터셋, time series, numerical만  
iii) 작은 데이터셋, categorical, numerical  
iv) 큰 데이터 셋 쭉..  


## 1. 결측치가 없는 데이터 셋에서 결측치를 만들어내고, 결과값 비교  
### 시도해볼 variation  
i) col의 수 (1->2->4..)  
ii) 결측치의 수 (10%->30%->50%, 근데 솔직히 50%면 col 자체를 버리는 게 나을 것 같은데)  
iii) col의 종류(1번 행, 2번 행 등) #근데 이 data set에는 categorical이 없으니까 다른 데이터 셋으로도 해볼 것 
iv) 

### 잘 대체되였는지 확인할 방법: 전체적인 분석이 달라졌는지 중점으로 확인  
i) 수치적 비교: 기본적인 대푯값(mean,median, mode, variance)  
ii) 시각적 비교: kde 함수


####  clustering을 사용하는 것에 대한 의문들..
clustering은 missing value를 대체한 다음에 이용가능함  
categorical한 변수들을 포함하면 문제가 생길 가능성(왜냐하면 유클리드 거리를 쓰기 때문)  
그리고 high dimension에서는 시간이 오래 걸릴듯 (이건 이미 dbscan에서 본 문제)  
parameter은 어떻게 정할 것인가  

#### 그래서 대신 사용할 수 있는 방법들을 생각해보자 -한계: CLUSTERING WITH MISSING VALUE에 관한 논문이 없음... 
1. 결측치 있는 col을 제외하고 clustering을 해보자! <- 그렇지만 그런 col이 많아진다면 대처가 불가능해질 듯  
2. 
    - 일단 먼저 단일 대체(mean,mode) + missing indicator 칼럼을 넣음(그런데 이게 칼럼이 많아지면 어떻게 넣을지도 고민해봐야 함)
    - clustering을 돌리고 
    - 대체했던 것들 drop 시키고 그 다음에 group을 봐서 대체하는 것
3. 통조입에서 배웠던 hot deck 대체 (근데 이건 clustering은 아님)
4. KNNIMPUTER  
  
5. 회귀곡선
6. 상관도
