from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from DataBasehandler.models import *
from .models import AttemptAnswer
from Authentication.models import ExamData

def django(req):
    if req.user.is_authenticated:
        py = list(DjangoQues.objects.all())
        q = req.POST.get("ids")
        ans = req.POST.get("answer")

        # First question load
        if not q:
            q = 0
            req.session["correct_ans"] = 0
            req.session["question_no"] = 0
            req.session["visited"] = []

        else:
            q = int(q)
            correct_ans = req.session.get("correct_ans", 0)
            question_no = req.session.get("question_no", 0)
            visited = req.session.get("visited", [])
            # Check correct ans and upload it to database with ques, choosen answer, correct ans
            qid = req.POST.get("idss")
            attemp_ans = DjangoQues.objects.get(pk=qid)
            qs = attemp_ans.question
            tmp = ""
            if ans:
                tmp = ans
            else:
                tmp = "not Attempt"
            cr = attemp_ans.correct_answer
            sub = "Django"
            duplicate = AttemptAnswer.objects.filter(chk_id=qid).exists()
            if not duplicate:
                load_data = AttemptAnswer(
                    user=req.user,
                    question=qs,
                    selected_answer=tmp,
                    correct_answer=cr,
                    subject=sub,
                    chk_id=qid,
                )
                load_data.save()
            else:
                AttemptAnswer.objects.filter(chk_id=qid).update(selected_answer=tmp)

            if q - 1 < len(py):
                question = py[q - 1]
                qid = question.id

                #  Count once, even if skipped
                if qid not in visited:
                    if ans and question.correct_answer == ans:
                        correct_ans += 1
                    question_no += 1  # ✅ Count as attempted even if skipped
                    visited.append(qid)

                req.session["visited"] = visited
                req.session["correct_ans"] = correct_ans
                req.session["question_no"] = question_no

        #  Final submit
        if req.POST.get("submit") == "1":
            correct_ans = req.session.get("correct_ans", 0)
            question_no = req.session.get("question_no", 0)
            visited = req.session.get("visited", [])
            # Check correct ans and upload it to database with ques, choosen answer, correct ans
            qid = req.POST.get("idss")
            attemp_ans = DjangoQues.objects.get(pk=qid)
            qs = attemp_ans.question
            tmp = ""
            if ans:
                tmp = ans
            else:
                tmp = "not Attempt"
            cr = attemp_ans.correct_answer
            sub = "Django"
            duplicate = AttemptAnswer.objects.get(chk_id=qid)
            if not duplicate:
                load_data = AttemptAnswer(
                    user=req.user,
                    question=qs,
                    selected_answer=tmp,
                    correct_answer=cr,
                    subject=sub,
                    chk_id=qid,
                )
                load_data.save()
            else:
                AttemptAnswer.objects.filter(chk_id=qid).update(selected_answer=tmp)

            if q:
                q = int(q)
                if q < len(py):
                    question = py[q]
                else:
                    question = py[-1]
                qid = question.id

                #  Count last question if not visited
                if qid not in visited:
                    if ans and question.correct_answer == ans:
                        correct_ans += 1
                    question_no += 1  #  Count as attempted even if skipped
                    visited.append(qid)

        
            # Clear session
            req.session.pop("correct_ans", None)
            req.session.pop("question_no", None)
            req.session.pop("visited", None)

            # Render result over result page,,, and deleted the attemped Answer data

            tmp = AttemptAnswer.objects.filter(user=req.user, subject="Django")
            final_res = list(tmp)
            marks_scored = 0
            for i in final_res:
                if i.correct_answer == i.selected_answer:
                    marks_scored += 1
            tmp.delete()
            
            # Upload final result such as total marks and obtained marks in Exam data Database-------
            if ExamData.objects.filter(user=req.user, subject='Django',is_submitted=True).exists():
                messages.error(req,'Test already submitted')
                return HttpResponseRedirect('/')
            else:
                sub = "Django"
                marks_scored = correct_ans
                total = question_no
                exd = ExamData(
                    user=req.user,
                    marks_obtained=marks_scored,
                    total_marks=total,
                    subject=sub,
                    is_submitted=True
                )
                exd.save()
            return render(
                req, "result.html", {"result": final_res, "total_marks": marks_scored}
            )

        return render(
            req,
            "test.html",
            {
                "ques": py[q],
                "total": len(py) - 1,
                "current": q,
                "totalplus": len(py),
            },
        )
    else:
        messages.warning(req, "Login required for accessing test")
        return HttpResponseRedirect("/user/log_in")


def python(req):
    if req.user.is_authenticated:
        py = list(PythonQues.objects.all())
        q = req.POST.get("ids")
        ans = req.POST.get("answer")

        # First question load
        if not q:
            q = 0
            req.session["correct_ans"] = 0
            req.session["question_no"] = 0
            req.session["visited"] = []

        else:
            q = int(q)
            correct_ans = req.session.get("correct_ans", 0)
            question_no = req.session.get("question_no", 0)
            visited = req.session.get("visited", [])
            # Check correct ans and upload it to database with ques, choosen answer, correct ans
            qid = req.POST.get("idss")
            attemp_ans = PythonQues.objects.get(pk=qid)
            qs = attemp_ans.question
            tmp = ""
            if ans:
                tmp = ans
            else:
                tmp = "not Attempt"
            cr = attemp_ans.correct_answer
            sub = "Python"
            duplicate = AttemptAnswer.objects.filter(chk_id=qid).exists()
            if not duplicate:
                load_data = AttemptAnswer(
                    user=req.user,
                    question=qs,
                    selected_answer=tmp,
                    correct_answer=cr,
                    subject=sub,
                    chk_id=qid,
                )
                load_data.save()
            else:
                AttemptAnswer.objects.filter(chk_id=qid).update(selected_answer=tmp)

            if q - 1 < len(py):
                question = py[q - 1]
                qid = question.id

                #  Count once, even if skipped
                if qid not in visited:
                    if ans and question.correct_answer == ans:
                        correct_ans += 1
                    question_no += 1  # ✅ Count as attempted even if skipped
                    visited.append(qid)

                req.session["visited"] = visited
                req.session["correct_ans"] = correct_ans
                req.session["question_no"] = question_no

        #  Final submit
        if req.POST.get("submit") == "1":
            correct_ans = req.session.get("correct_ans", 0)
            question_no = req.session.get("question_no", 0)
            visited = req.session.get("visited", [])

            # Check correct ans and upload it to database with ques, choosen answer, correct ans
            qid = req.POST.get("idss")
            attemp_ans = PythonQues.objects.get(pk=qid)
            qs = attemp_ans.question
            tmp = ""
            if ans:
                tmp = ans
            else:
                tmp = "not Attempt"
            cr = attemp_ans.correct_answer
            sub = "Python"
            duplicate = AttemptAnswer.objects.get(chk_id=qid)
            if not duplicate:
                load_data = AttemptAnswer(
                    user=req.user,
                    question=qs,
                    selected_answer=tmp,
                    correct_answer=cr,
                    subject=sub,
                    chk_id=qid,
                )
                load_data.save()
            else:
                AttemptAnswer.objects.filter(chk_id=qid).update(selected_answer=tmp)

            if q:
                q = int(q)
                if q < len(py):
                    question = py[q]
                else:
                    question = py[-1]
                qid = question.id

                #  Count last question if not visited
                if qid not in visited:
                    if ans and question.correct_answer == ans:
                        correct_ans += 1
                    question_no += 1  #  Count as attempted even if skipped
                    visited.append(qid)


            # Clear session
            req.session.pop("correct_ans", None)
            req.session.pop("question_no", None)
            req.session.pop("visited", None)

            # Render result over result page,,, and deleted the attemped Answer data

            tmp = AttemptAnswer.objects.filter(user=req.user, subject="Python")
            final_res = list(tmp)
            marks_scored = 0
            for i in final_res:
                if i.correct_answer == i.selected_answer:
                    marks_scored += 1
            tmp.delete()
            
            # Upload final result such as total marks and obtained marks in Exam data Database-------
            if ExamData.objects.filter(user=req.user, subject='Python',is_submitted=True).exists():
                messages.error(req,'Test already submitted')
                return HttpResponseRedirect('/')
            else:
                sub = "Python"
                marks_scored = correct_ans
                total = question_no
                exd = ExamData(
                    user=req.user,
                    marks_obtained=marks_scored,
                    total_marks=total,
                    subject=sub,
                    is_submitted=True
                )
                exd.save()
            return render(
                req, "result.html", {"result": final_res, "total_marks": marks_scored}
            )

        return render(
            req,
            "test.html",
            {
                "ques": py[q],
                "total": len(py) - 1,
                "current": q,
                "totalplus": len(py),
            },
        )
    else:
        messages.warning(req, "Login required for accessing test")
        return HttpResponseRedirect("/user/log_in")


def cpp(req):
    if req.user.is_authenticated:
        py = list(CppQues.objects.all())
        q = req.POST.get("ids")
        ans = req.POST.get("answer")

        # First question load
        if not q:
            q = 0
            req.session["correct_ans"] = 0
            req.session["question_no"] = 0
            req.session["visited"] = []

        else:
            q = int(q)
            correct_ans = req.session.get("correct_ans", 0)
            question_no = req.session.get("question_no", 0)
            visited = req.session.get("visited", [])
            # Check correct ans and upload it to database with ques, choosen answer, correct ans
            qid = req.POST.get("idss")
            attemp_ans = CppQues.objects.get(pk=qid)
            qs = attemp_ans.question
            tmp = ""
            if ans:
                tmp = ans
            else:
                tmp = "not Attempt"
            cr = attemp_ans.correct_answer
            sub = "Cpp"
            duplicate = AttemptAnswer.objects.filter(chk_id=qid).exists()
            if not duplicate:
                load_data = AttemptAnswer(
                    user=req.user,
                    question=qs,
                    selected_answer=tmp,
                    correct_answer=cr,
                    subject=sub,
                    chk_id=qid,
                )
                load_data.save()
            else:
                AttemptAnswer.objects.filter(chk_id=qid).update(selected_answer=tmp)

            if q - 1 < len(py):
                question = py[q - 1]
                qid = question.id

                #  Count once, even if skipped
                if qid not in visited:
                    if ans and question.correct_answer == ans:
                        correct_ans += 1
                    question_no += 1  # ✅ Count as attempted even if skipped
                    visited.append(qid)

                req.session["visited"] = visited
                req.session["correct_ans"] = correct_ans
                req.session["question_no"] = question_no

        #  Final submit
        if req.POST.get("submit") == "1":
            correct_ans = req.session.get("correct_ans", 0)
            question_no = req.session.get("question_no", 0)
            visited = req.session.get("visited", [])
            # Check correct ans and upload it to database with ques, choosen answer, correct ans
            qid = req.POST.get("idss")
            attemp_ans = CppQues.objects.get(pk=qid)
            qs = attemp_ans.question
            tmp = ""
            if ans:
                tmp = ans
            else:
                tmp = "not Attempt"
            cr = attemp_ans.correct_answer
            sub = "Cpp"
            duplicate = AttemptAnswer.objects.get(chk_id=qid)
            if not duplicate:
                load_data = AttemptAnswer(
                    user=req.user,
                    question=qs,
                    selected_answer=tmp,
                    correct_answer=cr,
                    subject=sub,
                    chk_id=qid,
                )
                load_data.save()
            else:
                AttemptAnswer.objects.filter(chk_id=qid).update(selected_answer=tmp)

            if q:
                q = int(q)
                if q < len(py):
                    question = py[q]
                else:
                    question = py[-1]
                qid = question.id

                #  Count last question if not visited
                if qid not in visited:
                    if ans and question.correct_answer == ans:
                        correct_ans += 1
                    question_no += 1  #  Count as attempted even if skipped
                    visited.append(qid)



            # Clear session
            req.session.pop("correct_ans", None)
            req.session.pop("question_no", None)
            req.session.pop("visited", None)

            # Render result over result page,,, and deleted the attemped Answer data

            tmp = AttemptAnswer.objects.filter(user=req.user, subject="Cpp")
            final_res = list(tmp)
            marks_scored = 0
            for i in final_res:
                if i.correct_answer == i.selected_answer:
                    marks_scored += 1
            tmp.delete()
            
            # Upload final result such as total marks and obtained marks in Exam data Database-------
            if ExamData.objects.filter(user=req.user, subject='Cpp',is_submitted=True).exists():
                messages.error(req,'Test already submitted')
                return HttpResponseRedirect('/')
            else:
                sub = "Cpp"
                marks_scored = correct_ans
                total = question_no
                exd = ExamData(
                    user=req.user,
                    marks_obtained=marks_scored,
                    total_marks=total,
                    subject=sub,
                    is_submitted=True
                )
                exd.save()
            return render(
                req, "result.html", {"result": final_res, "total_marks": marks_scored}
            )

        return render(
            req,
            "test.html",
            {
                "ques": py[q],
                "total": len(py) - 1,
                "current": q,
                "totalplus": len(py),
            },
        )
    else:
        messages.warning(req, "Login required for accessing test")
        return HttpResponseRedirect("/user/log_in")


def java(req):
    if req.user.is_authenticated:
        py = list(JavaQues.objects.all())
        q = req.POST.get("ids")
        ans = req.POST.get("answer")

        # First question load
        if not q:
            q = 0
            req.session["correct_ans"] = 0
            req.session["question_no"] = 0
            req.session["visited"] = []

        else:
            q = int(q)
            correct_ans = req.session.get("correct_ans", 0)
            question_no = req.session.get("question_no", 0)
            visited = req.session.get("visited", [])
            # Check correct ans and upload it to database with ques, choosen answer, correct ans
            qid = req.POST.get("idss")
            attemp_ans = JavaQues.objects.get(pk=qid)
            qs = attemp_ans.question
            tmp = ""
            if ans:
                tmp = ans
            else:
                tmp = "not Attempt"
            cr = attemp_ans.correct_answer
            sub = "Java"
            duplicate = AttemptAnswer.objects.filter(chk_id=qid).exists()
            if not duplicate:
                load_data = AttemptAnswer(
                    user=req.user,
                    question=qs,
                    selected_answer=tmp,
                    correct_answer=cr,
                    subject=sub,
                    chk_id=qid,
                )
                load_data.save()
            else:
                AttemptAnswer.objects.filter(chk_id=qid).update(selected_answer=tmp)

            if q - 1 < len(py):
                question = py[q - 1]
                qid = question.id

                #  Count once, even if skipped
                if qid not in visited:
                    if ans and question.correct_answer == ans:
                        correct_ans += 1
                    question_no += 1  # ✅ Count as attempted even if skipped
                    visited.append(qid)

                req.session["visited"] = visited
                req.session["correct_ans"] = correct_ans
                req.session["question_no"] = question_no

        #  Final submit
        if req.POST.get("submit") == "1":
            correct_ans = req.session.get("correct_ans", 0)
            question_no = req.session.get("question_no", 0)
            visited = req.session.get("visited", [])
            # Check correct ans and upload it to database with ques, choosen answer, correct ans
            qid = req.POST.get("idss")
            attemp_ans = JavaQues.objects.get(pk=qid)
            qs = attemp_ans.question
            tmp = ""
            if ans:
                tmp = ans
            else:
                tmp = "not Attempt"
            cr = attemp_ans.correct_answer
            sub = "Java"
            duplicate = AttemptAnswer.objects.get(chk_id=qid)
            if not duplicate:
                load_data = AttemptAnswer(
                    user=req.user,
                    question=qs,
                    selected_answer=tmp,
                    correct_answer=cr,
                    subject=sub,
                    chk_id=qid,
                )
                load_data.save()
            else:
                AttemptAnswer.objects.filter(chk_id=qid).update(selected_answer=tmp)

            if q:
                q = int(q)
                if q < len(py):
                    question = py[q]
                else:
                    question = py[-1]
                qid = question.id

                #  Count last question if not visited
                if qid not in visited:
                    if ans and question.correct_answer == ans:
                        correct_ans += 1
                    question_no += 1  #  Count as attempted even if skipped
                    visited.append(qid)

            
            # Clear session
            req.session.pop("correct_ans", None)
            req.session.pop("question_no", None)
            req.session.pop("visited", None)

            # Render result over result page,,, and deleted the attemped Answer data

            tmp = AttemptAnswer.objects.filter(user=req.user, subject="Java")
            final_res = list(tmp)
            marks_scored = 0
            for i in final_res:
                if i.correct_answer == i.selected_answer:
                    marks_scored += 1
            tmp.delete()
            
            # Upload final result such as total marks and obtained marks in Exam data Database-------
            if ExamData.objects.filter(user=req.user, subject='Java',is_submitted=True).exists():
                messages.error(req,'Test already submitted')
                return HttpResponseRedirect('/')
            else:
                sub = "Java"
                marks_scored = correct_ans
                total = question_no
                exd = ExamData(
                    user=req.user,
                    marks_obtained=marks_scored,
                    total_marks=total,
                    subject=sub,
                    is_submitted=True
                )
                exd.save()
            return render(
                req, "result.html", {"result": final_res, "total_marks": marks_scored}
            )

        return render(
            req,
            "test.html",
            {
                "ques": py[q],
                "total": len(py) - 1,
                "current": q,
                "totalplus": len(py),
            },
        )
    else:
        messages.warning(req, "Login required for accessing test")
        return HttpResponseRedirect("/user/log_in")


def delete_exam_rec(req,id):
    if req.method=='POST':
        ExamData.objects.get(pk=id).delete()
        messages.success(req,'Exam Record deleted successfully')
    return HttpResponseRedirect('/user/profile/')


