///////////////////////////////////////////////////////////
//  vendigMachine.h
//  Implementation of the Class VendingMachine
//  Created on:      22-sep-2026 14:05:12
//  Original author: halaa
///////////////////////////////////////////////////////////

#if !defined(EA_68EE7554_CE1A_462d_9F3F_E940AC72CC73__INCLUDED_)
#define EA_68EE7554_CE1A_462d_9F3F_E940AC72CC73__INCLUDED_

#include "Soda.h"
#include <vector>

class VendingMachine
{

public:
	VendingMachine();
	virtual ~VendingMachine();
	std::vector<Soda> sodas;

	void addSoda(Soda soda);
	Soda getSoda();
	void printInventory();

};
#endif // !defined(EA_68EE7554_CE1A_462d_9F3F_E940AC72CC73__INCLUDED_)
