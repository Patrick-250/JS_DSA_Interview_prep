class Node{
    constructor(value){
        this.value=value,
        this.next=null
    }
}


class Stack{
    constructor(){
        this.array=[]

    }

    peek(){
        return this.array[this.array.length-1]
    }
    push(value){
        return this.array.push(value)

    }
    pop(value){
        return this.array.pop(value)
    }




}
mystack=new Stack()
mystack.push("amazon")
mystack.push("google")
mystack.pop() // pop google out... remove google
console.log(mystack)