#include	<iostream>
using namespace std;

class SomeClass {
	public:
	
	SomeClass(string name,int var2){
		cout << "name is" << name << endl;
		var=var2 ;
	}
	~SomeClass() {
		cout << "Iam destructor" << endl;
}
	private:
	int var ;

	public:
		int SomeMethod(){
			cout << "Iam some Method" << endl;
}
};

	

int main ( char c , char* v[] )
{
	
	SomeClass someobj("umas",12);
	someobj.SomeMethod();
	return 0;

}
