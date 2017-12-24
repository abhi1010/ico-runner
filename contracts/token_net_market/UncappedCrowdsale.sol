/**
 * This smart contract code is Copyright 2017 TokenMarket Ltd. For more information see https://tokenmarket.net
 *
 * Licensed under the Apache License, version 2.0: https://github.com/TokenMarketNet/ico/blob/master/LICENSE.txt
 */

pragma solidity ^0.4.8;

import "./Crowdsalenet.sol";
import "./MintableTokenNet.sol";


/**
 * Uncapped ICO crowdsale contract.
 *
 *
 * Intended usage
 *
 * - A short time window
 * - Flat price
 * - No cap
 *
 */
contract UncappedCrowdsale is CrowdsaleNet {

  function UncappedCrowdsale(address _token, PricingStrategy _pricingStrategy, address _multisigWallet, uint _start, uint _end, uint _minimumFundingGoal) CrowdsaleNet(_token, _pricingStrategy, _multisigWallet, _start, _end, _minimumFundingGoal) {

  }

  function getRes() public constant returns (uint256) { return 2;}

  /**
   * Called from invest() to confirm if the curret investment does not break our cap rule.
   */
  function isBreakingCap(uint weiAmount, uint tokenAmount, uint weiRaisedTotal, uint tokensSoldTotal) constant returns (bool limitBroken) {
    return false;
  }

  function isCrowdsaleFull() public constant returns (bool) {
    // Uncle Scrooge
    return false;
  }

  function assignTokens(address receiver, uint tokenAmount) internal {
    MintableTokenNet mintableToken = MintableTokenNet(token);
    mintableToken.mint(receiver, tokenAmount);
  }
}
