// ���� �κ� ���ڿ� ������ DP Ǯ���̴�.
// ó������ ���ϴ� ���ڿ� �Է� �������µ�, C������ ���ڿ��� ���̸� ��������� �߾���.
// ������ C++���� �����ϴ� string Ŭ������ �̿��ϸ� getline()���� �����ϰ� �Է¹��� �� �ִ�.
#include <iostream>
#include <string>
using namespace std;


int main()
{
	string s1, s2;
	getline(cin, s1);
	getline(cin, s2);

	int L1, L2;
	L1 = s1.length();
	L2 = s2.length();
	
	// dp��� 2���� �迭�� ���� �Ҵ��ϴ� �κ�. int**�� new int*�� 2�� �����Ͱ� ����.
	int** dp = new int* [L1];
	for (int i = 0; i < L1; i++)
	{
		dp[i] = new int[L2];
	}

	// 2�� for���� ���鼭, s1�� s2�� ���ڿ��� ��ġ�� (i, j) ĭ�� ���ڸ� ǥ���Ѵ�.
	// (i-1, j-1) ĭ�� +1�� ǥ���ϸ� ���ӵǴ� ���ڿ��� ���̸� �ǹ��Ѵ�.
	int result = 0;
	for (int i = 0; i < L1; i++)
	{
		for (int j = 0; j < L2; j++)
		{
			if (s1[i] == s2[j])
			{
				if (i == 0 or j == 0)
				{
					dp[i][j] = 1;
				}
				else
				{
					dp[i][j] = dp[i - 1][j - 1] + 1;
					// dp�� ����Ǵ� ���� ū ���� result�� �Ҵ��Ѵ�.
					if (result < dp[i][j])
					{
						result = dp[i][j];
					}
				}
			}	
		}
	}

	// ���� �Ҵ� �� �޸� ���� ������ ���� �޸𸮸� ��������� �Ѵ�.
	for (int i = 0; i < L1; i++)
	{
		delete[] dp[i];
	}

	cout << result << endl;

	return 0;
}