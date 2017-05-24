
Test plan is for backend and fronted.  Backend test is in pyunit.

Showing input and expected output:

0 -> 0

1 -> 1

2 -> 1

3 -> 2

4 -> 3

negative number	-> 404

max signed int 2,147,483,647 -> 

lower case letter -> 404

upper case letter -> 404

char @	-> 404

In addition, some manual frontend test is done. 

Bug report:
- backend test:
1.  input value max signed integer 2147483647 takes a along time.  eventually test is killed.  Not sure if it is because I am running micro instance or due to other issues.  in production environment, ideally, we will test and see how long it will take.  if it times out, verify that reasonable error message is returned.

frontend test:
1.  error is not observed when invalid inputs are entered in.  It looks like the following changes is needed so that error is propagated to the frontend.  https://github.com/dmitryzv/dg-fibonacci-fe/blob/master/templates/index.html line 49, it should either be 
document.getElementById('number').value = jqXHR.resposeText;
or 
document.getElementById('number').value = textStatus;

2. just like backend test, input value max signed integer 2147483647 takes a along time.

3. enhancement.  in addition to mouseclick, form should be submitted upon pressing enter.  this is not observed using firefox and chrome.
