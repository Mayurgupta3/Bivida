from hash import hashturnover,hashExperience
import json


def makeTransaction(maxValue=3):

    import random
    sign = int(random.getrandbits(1))*2 - 1
    amount = random.randint(1,maxValue)
    turnover = 1
    experience = 0

    return {u'Turnover': turnover,u'Experience': experience}

def updateState(txn, state):

    state = state.copy()
    for key in txn:
        if key in state.keys():
            state[key] += txn[key]
        else:
            state[key] = txn[key]
    return state


state = {u'turnover': 0.0, u'exp': 0.0}  # Define the initial state
genesisBlockTxns = [state]
genesisBlockContents = {u'blockNumber':0,u'parentHash':None,u'txnCount':1,u'txns':genesisBlockTxns}
genesisHash = hashturnover( genesisBlockContents )
genesisHash = hashExperience( genesisBlockContents )
genesisBlock = {u'hash':genesisHash,u'contents':genesisBlockContents}
genesisBlockStr = json.dumps(genesisBlock, sort_keys=True)



def makeBlock(txns, chain):
    parentBlock = chain[-1]
    parentHash = parentBlock[u'hash']
    blockNumber = parentBlock[u'contents'][u'blockNumber'] + 1
    txnCount = len(txns)
    blockContents = {u'blockNumber': blockNumber, u'parentHash': parentHash,
                     u'txnCount': len(txns), 'txns': txns}
    blockHash = hashturnover(blockContents)
    blockHash = hashExperience(blockContents)
    block = {u'hash': blockHash, u'contents': blockContents}

    return block


blockSizeLimit = 5

while len(txnBuffer) > 0:
    bufferStartSize = len(txnBuffer)


    txnList = []
    while (len(txnBuffer) > 0) & (len(txnList) < blockSizeLimit):
        newTxn = txnBuffer.pop()
        validTxn = isValidTxn(newTxn, state)

        if validTxn:
            txnList.append(newTxn)
            state = updateState(newTxn, state)
        else:
            print("ignored transaction")
            sys.stdout.flush()
            continue

    ## Make a block
    myBlock = makeBlock(txnList, chain)
    x=chain.append(myBlock)

    return x