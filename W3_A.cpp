#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Node
{
public:
	Node* pre;
	vector<Node*> kid;
	string data;
	int result;
};

void setUp(Node* node)
{
	if(node->pre == NULL) //node�� root�϶� result�� ����
		node->result = node->data.size();
	else //root�� �ƴ� node�� result�� ����
	{
		node->result = node->pre->result + node->data.size() + 1;
	}
	
	if (node->kid.empty() == false) //Ʈ�������� ���� �������鼭 ����Լ� ȣ��
	{
		for(int i = 0; i < node->kid.size(); i++)
		{
			setUp(node->kid[i]);
		}
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
		int N;
		cin >> N;

		vector<Node> V(N + 1);
		V[1].pre = NULL;

		for (int i = 1; i < N; i++)//�ڽ� ���� �Է�
		{
			int A, B;
			cin >> A >> B;
			
			V[A].kid.push_back(&V[B]);
			V[B].pre = &V[A];
		}

		for (int i = 1; i <= N; i++)
		{
			string str;
			cin >> str;
			V[i].data = str;
		}
		setUp(&V[1]);
		for(int i = 1; i <= N; i++)
		{
			cout << V[i].result << "\n";
		}
	}
}
