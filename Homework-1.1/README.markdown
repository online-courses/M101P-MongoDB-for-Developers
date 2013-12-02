Task
===

Mongo should be installed, configured and running.

    cd hw1
    mongorestore dump

output something like this:

> connected to: 127.0.0.1
>
> Mon Dec  2 00:33:53.164 dump/m101/funnynumbers.bson
>
> Mon Dec  2 00:33:53.164     going into namespace [m101.funnynumbers]
100 objects found
>
> Mon Dec  2 00:33:53.166   Creating index: { key: { _id: 1 }, ns: "m101.funnynumbers", name: "_id_" }
>
> Mon Dec  2 00:33:53.169 dump/m101/hw1.bson
>
> Mon Dec  2 00:33:53.169   going into namespace [m101.hw1]
1 objects found
>
> Mon Dec  2 00:33:53.170   Creating index: { key: { _id: 1 }, ns: "m101.hw1", name: "_id_" }

Query the result

    use m101
    db.hw1.findOne()

output should be:

    {
        "_id" : ObjectId("50773061bf44c220307d8514"),
        "answer" : 42,
        "question" : "The Ultimate Question of Life, The Universe and Everything"
    }

so the value is `42`.
