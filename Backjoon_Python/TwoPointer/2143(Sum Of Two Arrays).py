#2143 두 배열의 합
t=int(input())
n=int(input())
n_array=list(map(int,input().split()))
m=int(input())
m_array=list(map(int,input().split()))
n_subarray=[]
m_subarray=[]
res=0
for i in range(n):
    temp_sum=0
    for j in range(i,n):
        temp_sum+=n_array[j]
        n_subarray.append(temp_sum)
for i in range(m):
    temp_sum=0
    for j in range(i,m):
        temp_sum+=m_array[j]
        m_subarray.append(temp_sum)
n_subarray.sort()
m_subarray.sort(reverse=True)
n_subarray_index=m_subarray_index=0
while n_subarray_index<len(n_subarray) and m_subarray_index<len(m_subarray):
    if n_subarray[n_subarray_index]+m_subarray[m_subarray_index]==t:
        if n_subarray_index+1<len(n_subarray) and n_subarray[n_subarray_index]==n_subarray[n_subarray_index+1]:
            if m_subarray_index+1<len(m_subarray) and m_subarray[m_subarray_index]==m_subarray[m_subarray_index+1]:
                tempn=1
                while n_subarray_index+1<len(n_subarray) and n_subarray[n_subarray_index]==n_subarray[n_subarray_index+1]:
                    tempn+=1
                    n_subarray_index+=1
                tempm=1
                while m_subarray_index+1<len(m_subarray) and m_subarray[m_subarray_index]==m_subarray[m_subarray_index+1]:
                    tempm+=1
                    m_subarray_index+=1
                res+=(tempn*tempm-1)
            else:
                n_subarray_index+=1
                res+=1
        else:
            m_subarray_index+=1
            res+=1
    elif n_subarray[n_subarray_index]+m_subarray[m_subarray_index]<t:
        n_subarray_index+=1
    else:
        m_subarray_index+=1
print(res)