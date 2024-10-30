from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def register(request):
    
    s="""
    <html>
    <body>
    <div class="full">
        <form>
            First Name: <input type="text" name="fname" id="fname"><br><br>
            Last Name: <input type="text" name="lname" id="lname"><br><br>
            Age: <input type="number" name="age" id="age"><br><br>
            DOB: <input type="date" id="dob" name="dob"><br><br>

            Username: <input type="text" id="uname" name="uname"><br><br>
            Password: <input type="password" id="pw" name="pw">
            Confirm Password: <input type="password" id="cpw" name="cpw"><br><br>

            e-mail: <input type="email"><br><br>
            Mobile Number: <input type="number" name="mob_num" id="mob_num"><br><br>

            Gender: <input type="radio" name="radio" value="Male" id="gender1">M
            <!-- <label for="gender1">M</label> -->
            <input type="radio" name="radio" value="Female" id="gender2">F
            <!-- <label for="gender2">F</label> -->
            <input type="radio" name="radio" value="others" id="gender3">Others<br><br>
            <!-- <label for="gender3">Others</label><br> -->


            Education: <select name="education" id="education">
                <option value="" disabled selected>select</option>
                <option value="SSLC">SSLC</option>
                <option value="B.Tech">B.Tech</option>
                <option value="M.Tech">M.Tech</option>
                <option value="PHD">PHD</option>
            </select><br><br>

            Hobbies:<br> <input type="checkbox" id="cb1">chess<br>
            <input type="checkbox" id="cb2">cricket<br>
            <input type="checkbox" id="cb3">football<br>
            <input type="checkbox" id="cb4">kabaddi<br><br>

            <table>
                <tr>
                  <th>A</th>
                  <th>B</th>
                  <th>C</th>
                </tr>
                <tr>
                  <td>x</td>
                  <td colspan="2">y</td>
                </tr>
                <tr>
                    <td rowspan="2">p</td>
                    <td>p<sup>2</sup></td>
                    <td>q<sub>2</sub></td>
                </tr>
                <tr>
                    <!-- <td rowspan="2">p</td> -->
                    <td>p<sup>3</sup></td>
                    <td>q<sub>3</sub></td>
                </tr>
            </table>

            <br><br>
            <input type="submit" value="submit">
            <input type="reset" value="reset">

        </form>
    </div>

</body>

</html>"""
    
    return HttpResponse(s)