from flask import request, redirect, url_for, render_template
from services.votesService import votesService
from abc import abstractmethod

# Get candidates
def _get():
    votes = votesService.get()
    
    print(votes)
    return render_template('votes.html', rick_votes=votes['Rick Sanchez'], jesus_votes=votes['Jesus Cristo'], darth_votes=votes['Darth Vader'], romer_votes=votes['Romer Simpson'], michael_votes=votes['Michael Jackson'])

# Update candiates votes 
def _update(request):
    candidate_name = request.form['candidate']
    success = votesService.updateVote(candidate_name)

    if success == True:
        return redirect(url_for('votes', candidate=candidate_name))

    else:
        print('Ocorreu um erro')
        return redirect(url_for('votes'), candidate_name='candidate_name')

class votesController():
    @abstractmethod
    def use(request):
        if request.method == 'GET': 
            return _get()

        else:
          return _update(request)