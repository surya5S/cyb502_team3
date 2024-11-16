// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract DocumentVerification {
    mapping(bytes32 => bool) private documentHashes;

    // Function to add a new document hash
    function addDocumentHash(bytes32 _hash) public {
        require(!documentHashes[_hash], "Document already exists!");
        documentHashes[_hash] = true;
    }

    // Function to verify a document hash
    function verifyDocumentHash(bytes32 _hash) public view returns (bool) {
        return documentHashes[_hash];
    }
}
