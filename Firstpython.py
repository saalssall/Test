
def job_a(duration, difficulty):

    hardjob = 7 # or higher
    shortjob = 3 # months or less

    if difficulty < hardjob:
        if duration > shortjob:
            # Job is easy and there's lots of time
            return 'Accept'
        else:
            # Job is easy but the deadline is short
            return 'Negotiate'          
    else:
        if duration > shortjob:
            # Job is hard but the deadline is long
            return 'Negotiate'
        else:
            # Job is hard and there's little time
            return 'Decline'

#---------------------------------------------------------------------
#
# Second solution - Using Boolean connectives
#
# Return an Accept/Negotiate/Decline string given the duration
# of a job, in months, and its level of difficulty, on a 1 to 10
# scale, as per our management quadchart, where durations of
# three months or less are considered "short" and jobs with a
# difficulty level of seven or more are considered "hard"
#
def job_b(duration, difficulty):

    hardjob = 7 # or higher
    shortjob = 3 # months or less

    if difficulty < hardjob and duration > shortjob:
        # Job easy and lots of time
        return 'Accept'
    elif difficulty >= hardjob and duration <= shortjob:
        # Job hard and little time
        return 'Decline'
    else:
        # Job is easy but the deadline is short or
        # job is hard but the deadline is long
        return 'Negotiate'


#---------------------------------------------------------------------
#
# Run the tests automatically
#
from doctest import testmod, REPORT_ONLY_FIRST_FAILURE
print(testmod(verbose = False,
              optionflags = REPORT_ONLY_FIRST_FAILURE))




# name.isalpha()
# name.islower()
# name.isnumeric()
# Returns Boolean values

