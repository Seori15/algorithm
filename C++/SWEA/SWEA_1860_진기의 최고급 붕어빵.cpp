#include <stdio.h>
#include <string.h> // char ����� ���� ���̺귯�� 
#include <algorithm> // sort ����� ���� ���̺귯�� 
using namespace std; // std ������ ���� namespace 

char result2[11] = "Impossible";

int main(void)
{
	int tc, T;
	scanf("%d", &T);
	for(tc = 0; tc < T; tc++)
	{
		int N, M, K, i;
		scanf("%d %d %d", &N, &M, &K);
		char result[9] = "Possible";
		int arr[N];
		for(i = 0; i < N; i++)
		{
			scanf("%d", &arr[i]);
		}
		sort(arr, arr+N);
		for(i = 0; i < N; i++)
		{
			if(arr[i]/M*K < i+1)
			{
				strcpy(result, result2); // for���� ���鼭 ���ǿ� ���� �ʴ´ٸ� result�� Impossible�� �ٲ� 
				break;
			}
		}
		printf("#%d %s\n", tc+1, result);
	}
	return 0;
 } 
