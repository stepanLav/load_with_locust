def stake_changes_by_address(address):
    query = '{\n    stakeChanges(orderBy:TIMESTAMP_ASC, filter:{address:{equalTo:\"%s\"}}){\n    nodes{\n          id\n        address\n        timestamp\n        amount\n        accumulatedAmount\n        type\n      }\n    }\n  }' % (address)
    return {"query": query}

def history_changes_by_address(address):
    query = '{ historyElements( after: null, first: 100, orderBy: TIMESTAMP_DESC,filter: { address:{ equalTo: \"%s\"},}) { pageInfo { startCursor, endCursor }, nodes { id timestamp address reward extrinsic transfer }}}' % (address)
    return {"query": query}

def revards_by_address(address):
    query = '{ historyElements( filter: { reward: { notEqualTo: \"null\"}, address: { equalTo: \"%s\"}  }) { nodes { reward }}}' % (address)
    return {"query": query}

def get_accounts_from_subscan(filter: str, row_number: int, page: int):
    return {"filter":"%s" % (filter),"row":int('%s' % (row_number)),"page":int('%s' % (page)),"order":"desc","order_field":"balance"}
