// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SecurityLogs {
    struct Log {
        uint timestamp;
        string message;
    }

    Log[] public logs;

    event NewLog(uint timestamp, string message);

    function addLog(string memory _message) public {
        logs.push(Log(block.timestamp, _message));
        emit NewLog(block.timestamp, _message);
    }

    function getLogsCount() public view returns (uint) {
        return logs.length;
    }
}
