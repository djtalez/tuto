// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;


contract tuto {
    string public welcome = "HelloWorld";


    function getWelcome() public view returns (string memory) {
        return welcome;
    }

    function setWelcome(string memory welcomeStr) public payable returns (bool) {
        welcome = welcomeStr;
        return true;
    }

    function add(int a, int b) public pure returns (int) {
        return a + b;
    }

}