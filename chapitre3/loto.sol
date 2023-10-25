// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

contract loterie {
    address public manager;
    address[] public players;

    constructor() {
        manager = msg.sender;
    }

    function enter() public payable  {
        require(msg.value > .01 ether , "La mise minimun est de 0.01 ether");
        players.push(msg.sender);
    }

    function triggerWinner() public restrictedToons {
        uint choosedPlayer = random() % players.length;
        address winner = players[choosedPlayer];
        payable(manager).transfer(1000000
        );
        payable(winner).transfer(address(this).balance);
        resetLoterie();
    }

    function random() private view returns (uint) {
        return uint(keccak256(abi.encodePacked(block.difficulty, block.timestamp, players)));
    }

    modifier restrictedToons() {
        require(msg.sender == manager, "Seul le manager peut effectuer l'op\u00e9ration");
        _;
    }

    function resetLoterie() private {
        players = new address[](0);
    }

    function getPlayers() public view returns (address[] memory) {
        return players;
    }

}