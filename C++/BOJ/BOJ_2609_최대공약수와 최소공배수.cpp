#include <iostream>

// 221017. ������ ����� ���� �Լ� ������ ���� ������ �����.
// �ܼ��� def�� �����ϴ� python�� �޸� ��ȯ���� ���� �Լ����� int, void ���� �ٿ���� �Ѵ�.
// �׸��� GCD�� �����ϴ� �������� tmp�� �̿��� a, b �� ������ ���� �ٲ��ִ� ������ �� �� �־���.

// �ִ����� GCD�� ã�� �Լ�. ��Ŭ���� ȣ������ �����̴�.
int GCD(int a, int b)
{
	int tmp;
	if (a >= b)
	{
		while (b > 0)
		{
			tmp = a;
			a = b;
			b = tmp % a;
		}
		return a;
	}
	else
	{
		while (a > 0)
		{
			tmp = b;
			b = a;
			a = tmp % b;
		}
		return b;
	}
}

int main()
{
	using namespace std;

	int x, y;
	cin >> x;
	cin >> y;

	int G = GCD(x, y);
	cout << G << endl;
	cout << x * y / G << endl;
	return 0;
}