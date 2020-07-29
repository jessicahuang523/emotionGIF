from category import category
from get_gif import get_gif_url

for i in range (1,44):

    cat = category(i)
    tenorArr = get_gif_url("tenor", cat)
    giphyArr = get_gif_url("giphy", cat)

    html_str = '''
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta content="text/html;charset=UTF-8" http-equiv="Content-Type" />
            <script src='https://s3.amazonaws.com/mturk-public/externalHIT_v1.js' type='text/javascript'></script>
        </head>
        <body>
            <form id="mturk_form" method="post" name="mturk_form">
                <input type="hidden" id="assignmentId" value="" name="assignmentId"/>

                <h2>Please take a look at the following GIFs and choose all appropriate emotions that you've perceived or are able to describe them. Multiple answers are accepted.</h2>
    '''

    for j in range(5):
        html_str = html_str + '<img src=' + tenorArr[j] + " width=200px/>"
        html_str = html_str + '<img src=' + giphyArr[j] + " width=200px/>" 

    html_str += '''
                <fieldset>
                    <p><input name="agree" type="checkbox" value="amusement"/>Amusement</p>
                    <p><input name="agree" type="checkbox" value="excitement"/>Excitement</p>
                    <p><input name="agree" type="checkbox" value="relief"/>Relief</p>
                    <p><input name="agree" type="checkbox" value="anger"/>Anger</p>
                    <p><input name="agree" type="checkbox" value="fear"/>Fear</p>
                    <p><input name="agree" type="checkbox" value="sadness"/>Sadness</p>
                    <p><input name="agree" type="checkbox" value="contempt"/>Contempt</p>
                    <p><input name="agree" type="checkbox" value="guilt"/>Guilt</p>
                    <p><input name="agree" type="checkbox" value="satisfaction"/>Satisfaction</p>
                    <p><input name="agree" type="checkbox" value="contentment"/>Contentment</p>
                    <p><input name="agree" type="checkbox" value="happiness"/>Happiness</p>
                    <p><input name="agree" type="checkbox" value="shame"/>Shame</p>
                    <p><input name="agree" type="checkbox" value="disgust"/>Disgust</p>
                    <p><input name="agree" type="checkbox" value="pleasure"/>Pleasure</p>
                    <p><input name="agree" type="checkbox" value="surprise"/>Surprise</p>
                    <p><input name="agree" type="checkbox" value="embarrassment"/>Embarrassment</p>
                    <p><input name="agree" type="checkbox" value="pride"/>Pride</p>
                </fieldset>
                <br>
                <input type="submit" />
            </form>
            <script language='Javascript'>turkSetAssignmentID();</script>
        </body>
    </html>
    '''

    file_name = cat + '.html'
    with open(file_name, "w") as file:
        file.write(html_str)
    print( i ,"done")


print ("done")