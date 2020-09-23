const textArea = document.getElementById("textarea");
const name1 = document.getElementById("name1").innerHTML;
const name2 = document.getElementById("name2").innerHTML;
let lastMessageTime = document.getElementById("lastMessage").innerHTML;

setInterval(()=>
{
    fetch('/message-history/update', 
    {
        method: 'POST',
        headers: 
        {
    'Content-Type': 'application/json;charset=utf-8'
        },
  body: JSON.stringify(
        {
    'fromUser': name1,
    'toUser': name2,
    'lastMessage':lastMessageTime
        })
    })
    .then(response => response.json())
    .then(result => 
    {
        if(result.status == 'No new messages'){}
        else
        {
            lastMessageTime = result.lastMessageTime;
            textArea.value += "" +result.messages;
        }
    })

}, 2000);