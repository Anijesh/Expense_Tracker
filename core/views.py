from django.shortcuts import render, redirect
from .models import CurrentBalance, TrackingHistory
from django.contrib import messages

def index(request):
    # Handle form submission
    if request.method == 'POST':
        description = request.POST.get('description')
        amount = float(request.POST.get('amount', 0))

        current_balance, _ = CurrentBalance.objects.get_or_create(id=1)

        if amount == 0:
            messages.error(request, "Amount can't be zero")
            return redirect('/')

        expense_type = 'CREDIT' if amount > 0 else 'DEBIT'

        # Create transaction
        transaction = TrackingHistory.objects.create(
            amount=amount,
            expense_type=expense_type,
            current_balance=current_balance,
            description=description
        )

        # Update balance
        current_balance.current_balance += amount
        current_balance.save()

        return redirect('/')

    # Display page
    your_balance, _ = CurrentBalance.objects.get_or_create(id=1)
    income = 0
    expense = 0

    for transaction in TrackingHistory.objects.all():
        if transaction.expense_type == "CREDIT":
            income += float(transaction.amount)
        else:
            expense += abs(float(transaction.amount))

    context = {
        'income': income,
        'expense': expense,
        'transactions': TrackingHistory.objects.all(),
        'current_balance': your_balance
    }

    return render(request, 'index.html', context)


def delete_transaction(request, id):
    transaction = TrackingHistory.objects.filter(id=id).first()

    if transaction:
        current_balance, _ = CurrentBalance.objects.get_or_create(id=1)

        # Adjust balance based on type
        if transaction.expense_type == 'CREDIT':
            current_balance.current_balance -= transaction.amount
        else:  # DEBIT
            current_balance.current_balance += abs(transaction.amount)

        current_balance.save()
        transaction.delete()

    return redirect('/')
