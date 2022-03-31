function solution(s)
{
    const stack = [];
    for(let i = 0; i < s.length; i++) {
        let flag = false;
        while (stack.length > 0 && stack[stack.length-1] === s[i]) {
            stack.pop();
            flag = true;
        }
        if(!flag) {
            stack.push(s[i]);    
        }
        
    }
    console.log(stack);
    if(stack.length > 0) {
        return 0;
    }
    else {
        return 1;
    }
}