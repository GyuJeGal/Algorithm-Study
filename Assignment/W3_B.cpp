#include <iostream>
#include <vector>
#include <queue>

using namespace std;

class Node 
{
public:
	Node() { pre = NULL, result = 0, max = 0, second_max = 0; }; //�ʱⰪ 0���� ����, �߿�!
	Node* pre;
	vector<int> data; //������ ������ length��
	vector<Node*> cnt; //������ ����
	int result;
	int max, second_max;
};

void traversal(Node* node)
{
	if (node->pre == NULL) //node�� ���۳���� ��
	{
		priority_queue<int> Q;

		for (int i = 0; i < node->cnt.size(); i++)
		{
			node->cnt[i]->pre = node;
			node->cnt[i]->result = node->result; //���۳�带 ������ result���� �����Ǿ�� �ϹǷ� ���������� ������ ���ߵ�
			traversal(node->cnt[i]);
			int n = node->data[i] + node->cnt[i]->max;
			Q.push(n);
		}

		if (node->cnt.size() == 1) //���۳���� �ڽ��� �ϳ� �ۿ� ������, ���� for�� ���� 
								   //�켱����ť�� ���� �ϳ��ۿ� ������� ����. �׷��� ��������� ��
		{
			node->max = Q.top();
			Q.pop();
		}
		else
		{
			node->max = Q.top();
			Q.pop();
			node->second_max = Q.top();
		}
		int n = node->max + node->second_max;

		if (n > node->result)
		{
			cout << n << "\n";
		}
		else
		{
			cout << node->result << "\n";
		}
	}
	else if (node->cnt.size() == 1) //node�� leaf����� ��
	{
		if (node->pre == node->cnt[0])
		{
			node->max = node->second_max = 0;
		}
	}
	else //��尡 ���۳��, leaf��嵵 �ƴҶ� //�߰� ����� ��
	{
		priority_queue<int> Q;
		for (int i = 0; i < node->cnt.size(); i++)
		{
			if (node->pre != node->cnt[i])
			{
				node->cnt[i]->pre = node;
				node->cnt[i]->result = node->result;
				traversal(node->cnt[i]);
				int n = node->data[i] + node->cnt[i]->max;
				Q.push(n);
			}
		}
		if (node->cnt.size() == 2) //����� �ڽ��� �ϳ� �ۿ� ������, ���� for�� ���� 
								   //�켱����ť�� ���� �ϳ��ۿ� ������� ����. �׷��� ��������� ��
		{
			node->max = Q.top();
			Q.pop();
		}
		else
		{
			node->max = Q.top();
			Q.pop();
			node->second_max = Q.top();
		}

		int n = node->max + node->second_max;
		if (n > node->result)
		{
			node->result = n;
		}
		node->pre->result = node->result; //result�� �״�� �θ���� �ø���

	}
	
}

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int T;
	cin >> T;
	while (T--)
	{
		int n;
		cin >> n;
		vector<Node> V(n + 1);
		for (int i = 1; i < n; i++)
		{
			int a, b, c;
			cin >> a >> b >> c;
			V[a].cnt.push_back(&V[b]);
			V[a].data.push_back(c);
			V[b].cnt.push_back(&V[a]);
			V[b].data.push_back(c);
		}

		traversal(&V[1]);
	}
}