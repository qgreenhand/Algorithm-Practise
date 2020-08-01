#coding=utf-8
# 本题为考试多行输入输出规范示例，无需提交，不计分。
import sys
if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    ans = 0
    nums=[]
    for i in range(n):
        # 读取每一行
        nums.append( sys.stdin.readline().strip())
        
    def test(n:str):
        n=int(n)
        dp=[0]*(n+1)
        if n>=2:
            #n==2时必输
            dp[2]=0
        if n>=3:
            dp[3]=0

            for i in range(3,n+1):
                maxdo = i // 3
                #第一回合最多抽牌为三分之一否则下一步必输
                winflag=0
                for j in range(1,maxdo+1):
                    for k in range(1,j*2+1):
                        if dp[i-j-k]==1:
                            winflag=1
                            break
                    if winflag==1:
                        break
                dp[i]=winflag
        return dp[n]
    res=0
    for i in nums:
        if test(i)==1:
            res+=1
    print(res)