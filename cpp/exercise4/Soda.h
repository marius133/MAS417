///////////////////////////////////////////////////////////
//  Soda.h
//  Implementation of the Class Soda
//  Created on:      22-sep-2026 13:44:28
//  Original author: halaa
///////////////////////////////////////////////////////////

#if !defined(EA_0B7BF774_1625_4f40_B228_346F5188F695__INCLUDED_)
#define EA_0B7BF774_1625_4f40_B228_346F5188F695__INCLUDED_

class Soda
{

public:
	Soda();
	virtual ~Soda();

	double getPrice();
	void print();

private:
	int amount;
	string name;
	double price;

};
#endif // !defined(EA_0B7BF774_1625_4f40_B228_346F5188F695__INCLUDED_)
