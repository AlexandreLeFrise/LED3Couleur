
import asyncio
import logging

from asyncua import Client

async def main():
    url = "opc.tcp://10.4.1.146:4840/Charlie Serv/"
    async with Client(url=url) as client:
        print("pipipoopoo")
        bleu = client.get_node("ns=2;i=3")
        rouge = client.get_node("ns=2;i=2")
        vert = client.get_node("ns=2;i=4")

        await bleu.set_value(False)
        await rouge.set_value(False)
        await vert.set_value(False)

        LED = client.get_node("ns=2;i=1")
        await LED.call_method("2:Fermer")


if __name__=="__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Fin")



