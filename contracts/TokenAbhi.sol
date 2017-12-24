pragma solidity ^0.4.18;


import "./zeppelin/examples/SimpleToken.sol";

 /**
  * @title Ownable
  * @dev The Ownable contract has an owner address, and provides basic authorization control
  * functions, this simplifies the implementation of "user permissions".
  */
 contract TokenAbhi is SimpleToken {


  /**
   * @dev Constructor that gives msg.sender all of existing tokens.
   */
  function TokenAbhi() public {
    // totalSupply = INITIAL_SUPPLY;
    // balances[msg.sender] = INITIAL_SUPPLY;
  }

 }
