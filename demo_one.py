from syncano import client

with client.SyncanoApi(instance_name, apikey) as syncano:
    project = syncano.project_new('test', message_id=1)
    project_id = project['data']['project']['id']
    syncano.project_update(project_id, 'test_2', message_id=2)
    print(syncano.project_get(message_id=3))
    syncano.project_delete(project_id)

# Or
with  client.SyncanoApi(instance_name, apikey) as syncano:

    project = syncano.project.new('test', message_id=1)
    project_id = project['data']['project']['id']
    syncano.project.update(project_id, 'test_2', message_id=2)
    print(syncano.project.get(message_id=3))
    syncano.project.delete(project_id)

#Subscribe and list to notifications, and pings

with  client.SyncanoAsyncApi(instance_name, apikey) as syncano:
    syncano.subscription_subscribe_project(your_project_id)
    while True:
        message =  syncano.get_message(blocking=False)
        if message:
            print ('message', message)
