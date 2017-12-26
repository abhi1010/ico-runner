#!/usr/bin/env bash


CHAIN=${CHAIN:-horton}
echo -e "CHAIN to be initialized as $CHAIN"

populus chain new $CHAIN
cd chains/$CHAIN
./init_chain.sh

echo -e "Run ./chains/$CHAIN/run_chain.sh"
