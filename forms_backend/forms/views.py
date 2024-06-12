from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework import status
from datetime import datetime,timedelta
import json

from .forms import RegisterSerializer
@api_view(['POST'])
def registration(request):
    if request.method == 'POST':
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from .models import Register
@api_view(['POST'])
@csrf_exempt  
def login(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')
        try:
            user = Register.objects.get(email=username, password=password)
            if request.data.get('endpoint') == 'AdminLogin' and user.role != 'Admin':
                return Response('Access denied', status=status.HTTP_403_FORBIDDEN)

            return Response({'message': 'Login successful', 'role': user.role, 'id': user.id, 'name': user.name}, status=status.HTTP_200_OK)
        except Register.DoesNotExist:
            return Response({'error': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)


from .forms import FrontOfficeSerializer
@api_view(['POST'])
@csrf_exempt
def frontoffice_data(request):
    if request.method == 'POST':
        serializer = FrontOfficeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from .forms import FirstFloorSerializer
@api_view(['POST'])
@csrf_exempt
def firstfloor_data(request):
    if request.method == 'POST':
        serializer = FirstFloorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

from .forms import SecondFloorSerializer
@api_view(['POST'])
@csrf_exempt
def secondfloor_data(request):
    if request.method == 'POST':
        serializer = SecondFloorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

from .forms import ThirdFloorSerializer
@api_view(['POST'])
@csrf_exempt
def thirdfloor_data(request):
    if request.method == 'POST':
        serializer = ThirdFloorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from .forms import FirstSuitSerializer
@api_view(['POST'])
@csrf_exempt
def firstsuit_data(request):
    if request.method == 'POST':
        serializer = FirstSuitSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

from .forms import SecondSuitSerializer
@api_view(['POST'])
@csrf_exempt
def secondsuit_data(request):
    if request.method == 'POST':
        serializer = SecondSuitSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

from .forms import LabSerializer
@api_view(['POST'])
@csrf_exempt
def lab_data(request):
    if request.method == 'POST':
        serializer = LabSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

from .forms import CTSerializer
@api_view(['POST'])
@csrf_exempt
def CT_data(request):
    if request.method == 'POST':
        serializer = CTSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

from .forms import MRISerializer
@api_view(['POST'])
@csrf_exempt
def MRI_data(request):
    if request.method == 'POST':
        serializer = MRISerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

from .forms import XraySerializer
@api_view(['POST'])
@csrf_exempt
def Xray_data(request):
    if request.method == 'POST':
        serializer = XraySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

from .forms import OPDSerializer
@api_view(['POST'])
@csrf_exempt
def OPD_data(request):
    if request.method == 'POST':
        serializer = OPDSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

from .forms import OTSerializer
@api_view(['POST'])
@csrf_exempt
def OT_data(request):
    if request.method == 'POST':
        serializer = OTSerializer(request.POST)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

from .forms import HRSerializer
@api_view(['POST'])
def HR_data(request):
    if request.method == 'POST':
        serializer = HRSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

from .forms import PhysiotherapySerializer
@api_view(['POST'])
@csrf_exempt
def physiotherapy_data(request):
    if request.method == 'POST':
        serializer = PhysiotherapySerializer(request.POST)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

from .forms import DialysisSerializer
@api_view(['POST'])
@csrf_exempt
def dialysis_data(request):
    if request.method == 'POST':
        serializer = DialysisSerializer(request.POST)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

from .forms import OPPharmacySerializer
@api_view(['POST'])
@csrf_exempt
def OPPharmacy_data(request):
    if request.method == 'POST':
        serializer = OPPharmacySerializer(request.POST)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

from .forms import IPPharmacySerializer
@api_view(['POST'])
@csrf_exempt
def IPPharmacy_data(request):
    if request.method == 'POST':
        serializer = IPPharmacySerializer(request.POST)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

from .forms import EmergencyRoomSerializer
@api_view(['POST'])
@csrf_exempt
def emergency_room_data(request):
    if request.method == 'POST':
        serializer = EmergencyRoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from .forms import MRDSerializer
@api_view(['POST'])
@csrf_exempt
def MRD_data(request):
    if request.method == 'POST':
        serializer = MRDSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
from .forms import ChemoWardSerializer
@api_view(['POST'])
@csrf_exempt
def chemo_ward_data(request):
    if request.method == 'POST':
        serializer = ChemoWardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

from .forms import RecoveryWardSerializer
@api_view(['POST'])
@csrf_exempt
def recovery_ward_data(request):
    if request.method == 'POST':
        serializer = RecoveryWardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

from .forms import SICUSerializer
@api_view(['POST'])
@csrf_exempt
def SICU_data(request):
    if request.method == 'POST':
        serializer = SICUSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

from .forms import MICUSerializer
@api_view(['POST'])
@csrf_exempt
def MICU_data(request):
    if request.method == 'POST':
        serializer = MICUSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
from .forms import NICUSerializer
@api_view(['POST'])
@csrf_exempt
def NICU_data(request):
    if request.method == 'POST':
        serializer = NICUSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

from .forms import FirstFloorRawDataSerializer
@api_view(['POST'])
@csrf_exempt
def firstfloor_rawdata(request):
    if request.method == 'POST':
        data = request.data
        id = data.get('id')
        name = data.get('name')
        selected_date = data.get('selectedDate')
        raw_data = data.get('raw_data', [])

        if selected_date and raw_data:
            record_data = {
                'id': id,
                'name': name,
                'selectedDate': selected_date,
                'raw_data': raw_data
            }
            serializer = FirstFloorRawDataSerializer(data=record_data)

            if serializer.is_valid():
                serializer.save()
                return Response("Data submitted successfully", status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error": "selected_date and raw_data are required"}, status=status.HTTP_400_BAD_REQUEST)
        

from .forms import SecondSuitRawDataSerializer
@api_view(['POST'])
@csrf_exempt
def secondsuit_rawdata(request):
    if request.method == 'POST':
        data = request.data
        selected_date = data.get('selectedDate')
        raw_data = data.get('raw_data', [])

        if selected_date and raw_data:
            record_data = {
                'selectedDate': selected_date,
                'raw_data': raw_data
            }
            serializer = SecondSuitRawDataSerializer(data=record_data)

            if serializer.is_valid():
                serializer.save()
                return Response("Data submitted successfully", status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error": "selected_date and raw_data are required"}, status=status.HTTP_400_BAD_REQUEST)
        
    
from .forms import SecondFloorRawDataSerializer
@api_view(['POST'])
@csrf_exempt
def secondfloor_rawdata(request):
    if request.method == 'POST':
        data = request.data
        selected_date = data.get('selectedDate')
        raw_data = data.get('raw_data', [])

        if selected_date and raw_data:
            record_data = {
                'selectedDate': selected_date,
                'raw_data': raw_data
            }
            serializer = SecondFloorRawDataSerializer(data=record_data)

            if serializer.is_valid():
                serializer.save()
                return Response("Data submitted successfully", status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error": "selected_date and raw_data are required"}, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def get_export_data(request):
    if request.method == 'GET':
        ward = request.GET.get('ward')
        year = request.GET.get('year')
        month = request.GET.get('month')
        date = request.GET.get('date')
        
        query_params = {}

        if ward and date:
            query_params['ward'] = ward
            parsed_date = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%fZ")
            query_params['selectedDate'] = parsed_date.date()

        if ward and year and month:
            start_date = datetime(int(year), int(month), 1)
            end_date = start_date.replace(day=1, month=int(month)+1) if int(month) < 12 else start_date.replace(year=int(year)+1, month=1)
            query_params['ward'] = ward
            query_params['selectedDate__gte'] = start_date
            query_params['selectedDate__lt'] = end_date

        if query_params:
            try:
                selected_model = get_ward_model(ward)
                data = selected_model.objects.filter(**query_params).values()
                return JsonResponse(list(data), safe=False)
            except Exception as e:
                return JsonResponse({'error': str(e)}, status=500)
        else:
            return JsonResponse({'error': 'Please select a ward, year, and month'}, status=400)
    else:
        return JsonResponse({'error': 'Only GET requests are allowed'}, status=405)
    

@csrf_exempt
def update_export_data(request):
    if request.method == 'PUT':
        try:
            data = json.loads(request.body)
            for row in data:
                selected_date = datetime.strptime(row.get('selectedDate'), "%Y-%m-%dT%H:%M:%S.%fZ").date()
                ward = row.get('ward')
                selected_model = get_ward_model(ward)

                try:
                    # Update the record based on selected_date
                    existing_instance = selected_model.objects.get(selectedDate=selected_date)
                except selected_model.DoesNotExist:
                    return JsonResponse({'error': f'Instance with selectedDate {selected_date} does not exist'}, status=404)
                
                for key, value in row.items():
                    if key not in ['_id', 'ward', 'selectedDate']:
                        setattr(existing_instance, key, value)
                existing_instance.save()
                
            return JsonResponse({'success': 'Data updated successfully'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Only PUT requests are allowed'}, status=405)
    

@csrf_exempt
def get_export_rawdata(request):
    if request.method == 'GET':
        ward = request.GET.get('ward')
        year = request.GET.get('year')
        month = request.GET.get('month')
        date = request.GET.get('date')
        
        query_params = {}

        if ward and date:
            query_params['ward'] = ward
            parsed_date = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%fZ")
            query_params['selected_date'] = parsed_date.date()

        if ward and year and month:
            start_date = datetime(int(year), int(month), 1)
            end_date = start_date.replace(day=1, month=int(month)+1) if int(month) < 12 else start_date.replace(year=int(year)+1, month=1)
            query_params['ward'] = ward
            query_params['selected_date__gte'] = start_date
            query_params['selected_date__lt'] = end_date

        if query_params:
            try:
                selected_model = get_rawdata_model(ward)
                data = selected_model.objects.filter(**query_params).values()
                return JsonResponse(list(data), safe=False)
            except Exception as e:
                return JsonResponse({'error': str(e)}, status=500)
        else:
            return JsonResponse({'error': 'Please select a ward, year, and month'}, status=400)
    else:
        return JsonResponse({'error': 'Only GET requests are allowed'}, status=405)
    

@csrf_exempt
def update_export_rawdata(request):
    if request.method == 'PUT':
        try:
            data = json.loads(request.body)
            for row in data:
                selected_date = datetime.strptime(row.get('selectedDate'), "%Y-%m-%dT%H:%M:%S.%fZ").date()
                ward = row.get('ward')
                selected_model = get_ward_model(ward)

                try:
                    # Update the record based on selected_date
                    existing_instance = selected_model.objects.get(selectedDate=selected_date)
                except selected_model.DoesNotExist:
                    return JsonResponse({'error': f'Instance with selectedDate {selected_date} does not exist'}, status=404)
                
                for key, value in row.items():
                    if key not in ['_id', 'ward', 'selectedDate']:
                        setattr(existing_instance, key, value)
                existing_instance.save()
                
            return JsonResponse({'success': 'Data updated successfully'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Only PUT requests are allowed'}, status=405)


from .migrations.Views.constant import floor_beds
def availabilityofroomsandbeds(request, ward):
    try:
        # Get the corresponding model class based on the selected ward
        selected_model = get_ward_model.get(ward, None)
        print("selected_model",selected_model)
        if selected_model:
            # Query the selected model for occupancy date
            yesterday = datetime.today() - timedelta(days=1)
            print("date",yesterday)
            form_data = selected_model.objects.filter(selectedDate=yesterday).first()
            print("form_data",form_data)
            if form_data:
                # Access the correct field for the number of occupied beds
                occupied_beds = form_data.numberOfBedsOccupied
                print('occupied_beds_if',occupied_beds)
            else:
                # If no data is found, log a message for debugging
                print('No data found for the selected date')
                # If no data is found, occupied beds should be 0
                occupied_beds = 0
                print('occupied_beds_else',occupied_beds)
        else:
            # Handle cases where the ward type is not recognized or supported
            return JsonResponse({'error': 'Ward type not recognized'}, status=400)
        # Calculate the number of available beds using data from constants.py
        total_beds = floor_beds.get(ward, 0)  # Get total beds, default to 0 if ward not found
        available_beds = total_beds - int(occupied_beds)  # Convert occupied beds to integer before subtracting
        # Return the data in JSON format
        return JsonResponse({
            'ward': ward,
            'numberOfBedsOccupied': occupied_beds,
            'numberOfBedsAvailable': available_beds
        })
    except Exception as e:
        # Log the exception for debugging purposes
        print(f"Error: {e}")
        # Return a more descriptive error message
        return JsonResponse({'error': 'An error occurred while processing your request'}, status=500)
    

from .models import FrontOffice,FirstFloor,FirstSuit,SecondFloor,SecondSuit,ThirdFloor,Lab,CT,MRI,Xray  
from .models import OT,MRD,MICU,NICU,SICU,RecoveryWard,ChemoWard,Physiotherapy,Dialysis,EmergencyRoom,OPD,OPPharmacy
from collections import defaultdict

def get_formula_data(request):
    if request.method == 'GET':
        year = request.GET.get('year')
        month = request.GET.get('month')
        
        # Debugging: Print received parameters
        # print("Received parameters - year:", year, "month:", month)  
        
        query_params = {}

        if year and month:
            # Construct the start and end date for the selected month and year
            start_date = datetime(int(year), int(month), 1)
            end_date = start_date.replace(day=1, month=int(month)+1) if int(month) < 12 else start_date.replace(year=int(year)+1, month=1)
            query_params['selectedDate__gte'] = start_date
            query_params['selectedDate__lt'] = end_date

        # Debugging: Print query parameters
        # print("Query parameters:", query_params)  

        if query_params:  
            try:
                all_data = []
                totalNumberOfAdmissions = 0  # Initialize total admissions counter
                timeTakenForInitialAssessment = 0  # Initialize total time taken counter
                numberOfTestsPerformed = 0  # Initialize total admissions counter
                numberOfReportingErrors = 0  # Initialize total time taken counter
                numberOfStaffAdheringToSafety = 0
                numberOfStaffAudited = 0
                totalNumberOfOpportunitiesOfMedicationErrors = 0
                totalNumberOfMedicationErrors = 0
                numberOfTransfusionReactions = 0
                numberOfUnitsTransfused = 0
                actualDeathInICU = 0
                PredictedDeathsinICU = 0
                numberOfPatientsWhoDevelopNewOrWorseningOfPressureUlcer = 0
                totalNoOfRestraintPatientsDays = 0
                returnsToEmergency =0
                patientsToEmergency =0
                numberOfUrinaryCatheterAssociatedUTIsInMonth=0
                numberOfUrinaryCatheterDaysInMonth=0
                numberOfVentilatorAssociatedPneumonia=0
                numberOfVentilatorDays=0
                numberOfCentralLineAssociatedBloodStreamInfectionsInMonth=0
                numberOfCentralLineDaysInMonth=0
                numberOfSurgicalSiteInfectionsInMonth=0
                numberOfSurgicalSiteInfectionsInMonth=0
                timeTakenForBloodAndBloodComponents=0
                totalNoOfBloodAndBloodComponentsCrossMatched=0
                numberOfNursingStaff=0
                numberOfBedsOccupied=0
                numberOfPatientsDischarged=0
                timeTakenForDischarge=0
                NumberofMedicalRecords=0
                Numberofdischarge=0
                Numberofdeath=0
                waitingTimeForDiagnostics=0
                numberOfPatientsReportedInDiagnostics=0
                timeforconsultation=0
                TotalNumberofop=0
                numberOfNearMissReported=0
                numberOfIncidentsReported=0
                totalNoOfHandoversDoneAppropriately=0
                totalNoOfHandoverOpportunities=0
                totalNumberOfPrescriptionInCapitalLetters=0
                totalNumberOfPrescriptionSampled=0
                numberOfStockOutEmergencyDrugs=0
                numberOfInPatients=0
                numberOfPatientsDevelopingAdverseDrugReactions=0
                unplannedReturn=0
                procedureFollowed=0
                plannedSurgeries=0
                prophylacticAntibiotic=0
                rescheduledCases=0

                # Define a dictionary of model classes
                model_classes = {
        'Front Office': FrontOffice,
        'First Floor': FirstFloor,
        'First Suit': FirstSuit,
        'Second Floor': SecondFloor,
        'Second Suit': SecondSuit,
        'Third Floor': ThirdFloor,
        'Lab': Lab,
        'CT': CT,
        'MRI': MRI,
        'X-Ray': Xray,
        'OT': OT,
        'MRD': MRD,
        'MICU': MICU,
        'NICU': NICU,
        'SICU': SICU,
        'Recovery Ward': RecoveryWard,
        'Chemo Ward': ChemoWard,
        'Physiotherapy': Physiotherapy,
        'Dialysis': Dialysis,
        'ER': EmergencyRoom,
        'OPD':OPD,
        'OPPharmacy':OPPharmacy
                }

                # Inside the try block
                for ward, model in model_classes.items():
                    data = model.objects.filter(**query_params).values()
                    # print(f"Retrieved data for {ward}:", data)  # Add this line for debugging
                    all_data.extend(data)
                    for entry in data:
                        totalNumberOfAdmissions += int(entry.get('totalNumberOfAdmissions', 0))
                        timeTakenForInitialAssessment += int(entry.get('timeTakenForInitialAssessment', 0))
                        numberOfTestsPerformed += int(entry.get('numberOfTestsPerformed', 0))
                        numberOfReportingErrors += int(entry.get('numberOfReportingErrors', 0))
                        numberOfStaffAdheringToSafety += int(entry.get('numberOfStaffAdheringToSafety', 0))
                        numberOfStaffAudited += int(entry.get('numberOfStaffAudited', 0))
                        totalNumberOfOpportunitiesOfMedicationErrors += int(entry.get('totalNumberOfOpportunitiesOfMedicationErrors', 0))
                        totalNumberOfMedicationErrors += int(entry.get('totalNumberOfMedicationErrors', 0))
                        numberOfTransfusionReactions += int(entry.get('numberOfTransfusionReactions', 0))
                        numberOfUnitsTransfused += int(entry.get('numberOfUnitsTransfused', 0))
                        actualDeathInICU += int(entry.get('actualDeathInICU', 0))
                        PredictedDeathsinICU += int(entry.get('PredictedDeathsinICU', 0))
                        numberOfPatientsWhoDevelopNewOrWorseningOfPressureUlcer += int(entry.get('numberOfPatientsWhoDevelopNewOrWorseningOfPressureUlcer', 0))
                        totalNoOfRestraintPatientsDays += int(entry.get('totalNoOfRestraintPatientsDays', 0))
                        returnsToEmergency += int (entry.get('returnsToEmergency',0))
                        patientsToEmergency += int (entry.get('patientsToEmergency',0))
                        numberOfUrinaryCatheterAssociatedUTIsInMonth += int(entry.get('numberOfUrinaryCatheterAssociatedUTIsInMonth',0))
                        numberOfUrinaryCatheterDaysInMonth += int(entry.get('numberOfUrinaryCatheterDaysInMonth',0))
                        numberOfVentilatorAssociatedPneumonia += int (entry.get('numberOfVentilatorAssociatedPneumonia',0))
                        numberOfVentilatorDays += int (entry.get('numberOfVentilatorDays',0))
                        numberOfCentralLineDaysInMonth += int(entry.get('numberOfCentralLineDaysInMonth',0))
                        numberOfCentralLineAssociatedBloodStreamInfectionsInMonth += int(entry.get('numberOfCentralLineAssociatedBloodStreamInfectionsInMonth',0))
                        numberOfSurgicalSiteInfectionsInMonth += int(entry.get('numberOfSurgicalSiteInfectionsInMonth',0))
                        timeTakenForBloodAndBloodComponents += int(entry.get("timeTakenForBloodAndBloodComponents",0))
                        totalNoOfBloodAndBloodComponentsCrossMatched += int(entry.get('totalNoOfBloodAndBloodComponentsCrossMatched',0))
                        numberOfNursingStaff += int(entry.get('numberOfNursingStaff',0))
                        numberOfBedsOccupied += int(entry.get('numberOfBedsOccupied',0))
                        numberOfPatientsDischarged += int(entry.get('numberOfPatientsDischarged',0))
                        timeTakenForDischarge += int(entry.get('timeTakenForDischarge',0))
                        NumberofMedicalRecords += int (entry.get('NumberofMedicalRecords',0))
                        Numberofdischarge += int(entry.get('Numberofdischarge',0))
                        Numberofdeath += int(entry.get('Numberofdeath',0))
                        waitingTimeForDiagnostics += int(entry.get('waitingTimeForDiagnostics',0))
                        numberOfPatientsReportedInDiagnostics += int(entry.get('numberOfPatientsReportedInDiagnostics',0))
                        timeforconsultation += int(entry.get('timeforconsultation',0))
                        TotalNumberofop += int(entry.get('TotalNumberofop',0))
                        numberOfNearMissReported += int(entry.get('numberOfNearMissReported',0))
                        numberOfIncidentsReported += int (entry.get('numberOfIncidentsReported',0))
                        totalNoOfHandoversDoneAppropriately += int((entry.get('totalNoOfHandoversDoneAppropriately',0)))
                        totalNoOfHandoverOpportunities += int(entry.get('totalNoOfHandoverOpportunities',0))
                        totalNumberOfPrescriptionInCapitalLetters += int (entry.get('totalNumberOfPrescriptionInCapitalLetters',0))
                        totalNumberOfPrescriptionSampled += int (entry.get('totalNumberOfPrescriptionSampled',0))
                        numberOfStockOutEmergencyDrugs += int (entry.get('numberOfStockOutEmergencyDrugs',0))
                        numberOfPatientsDevelopingAdverseDrugReactions += int(entry.get('numberOfPatientsDevelopingAdverseDrugReactions',0))
                        numberOfInPatients += int(entry.get('numberOfInPatients',0))
                        unplannedReturn += int(entry.get('unplannedReturn',0))
                        procedureFollowed += int (entry.get('procedureFollowed',0))
                        plannedSurgeries += int(entry.get('plannedSurgeries',0))
                        prophylacticAntibiotic += int(entry.get('prophylacticAntibiotic',0))
                        rescheduledCases += int(entry.get('rescheduledCases',0))
                # Debugging: Print retrieved data
                # print("Retrieved data:", all_data)  

                # Calculate average time taken for initial assessment per admission
                average_time_taken = timeTakenForInitialAssessment / totalNumberOfAdmissions if totalNumberOfAdmissions > 0 else 0
                numberOfReportingErrors1 = numberOfReportingErrors / numberOfTestsPerformed if numberOfTestsPerformed > 0 else 0
                adherencetosafety = numberOfStaffAdheringToSafety / numberOfStaffAudited if numberOfStaffAudited > 0 else 0
                transfusedreactions = numberOfTransfusionReactions / numberOfUnitsTransfused if numberOfUnitsTransfused > 0 else 0
                totalNumberOfMedicationErrors = totalNumberOfMedicationErrors / totalNumberOfOpportunitiesOfMedicationErrors if totalNumberOfOpportunitiesOfMedicationErrors > 0 else 0
                morality_ratio_ICU = actualDeathInICU / PredictedDeathsinICU if PredictedDeathsinICU > 0 else 0
                ulcers_admission = numberOfPatientsWhoDevelopNewOrWorseningOfPressureUlcer / totalNoOfRestraintPatientsDays if totalNoOfRestraintPatientsDays  > 0 else 0
                return_of_emergency = returnsToEmergency/patientsToEmergency if patientsToEmergency >0 else 0
                catheterassociated_CDC_NHSN= numberOfUrinaryCatheterAssociatedUTIsInMonth/numberOfUrinaryCatheterDaysInMonth if numberOfUrinaryCatheterDaysInMonth >0 else 0
                ventilatorassociated_CDC_NHSN=numberOfVentilatorAssociatedPneumonia/numberOfVentilatorDays if numberOfVentilatorDays > 0 else 0
                bloodstrea_CDC_NHSN=numberOfCentralLineAssociatedBloodStreamInfectionsInMonth / numberOfCentralLineDaysInMonth if numberOfCentralLineDaysInMonth > 0 else 0
                available_transfusion= timeTakenForBloodAndBloodComponents / totalNoOfBloodAndBloodComponentsCrossMatched if totalNoOfBloodAndBloodComponentsCrossMatched > 0 else 0
                patient_ratio_icu=numberOfBedsOccupied / numberOfNursingStaff if  numberOfNursingStaff > 0 else 0
                time_taken_discharge= timeTakenForDischarge / numberOfPatientsDischarged if numberOfPatientsDischarged > 0 else 0
                numberofdischargesanddeaths=(Numberofdischarge + Numberofdeath )
                incomplete_improper_constent= NumberofMedicalRecords / numberofdischargesanddeaths if numberofdischargesanddeaths >0 else 0
                waiting_time_diagnostics = waitingTimeForDiagnostics / numberOfPatientsReportedInDiagnostics if numberOfPatientsReportedInDiagnostics >0 else 0
                time_outpatient_consultation=timeforconsultation / TotalNumberofop if TotalNumberofop  > 0 else 0
                near_misses=numberOfNearMissReported / numberOfIncidentsReported if numberOfIncidentsReported > 0 else 0
                handovers_shift_change=totalNoOfHandoversDoneAppropriately / totalNoOfHandoverOpportunities if totalNoOfHandoverOpportunities > 0 else 0                # Construct JSON response
                medication_prescription_capitals=totalNumberOfPrescriptionInCapitalLetters / totalNumberOfPrescriptionSampled if totalNumberOfPrescriptionSampled >0 else 0
                stock_outs_emergency_medications= numberOfStockOutEmergencyDrugs / 20 
                adverse_drug_reaction = numberOfPatientsDevelopingAdverseDrugReactions / numberOfInPatients if numberOfInPatients > 0 else 0
                unplanned_return_ot=unplannedReturn/procedureFollowed if procedureFollowed >0 else 0
                percentage_of_surgeries=procedureFollowed/plannedSurgeries if plannedSurgeries>0 else 0
                percentage_prophylacticAntibiotic=procedureFollowed/prophylacticAntibiotic if prophylacticAntibiotic >0 else 0
                re_scheduling_sugeries=rescheduledCases/procedureFollowed if procedureFollowed >0 else 0                
                response_data = {
                    # 'data': list(all_data),
                    'totalNumberOfAdmissions': totalNumberOfAdmissions,
                    'timeTakenForInitialAssessment': timeTakenForInitialAssessment,
                    'average_time_taken_per_admission': (int(average_time_taken)),
                    'numberOfTestsPerformed': numberOfTestsPerformed,
                    'numberOfReportingErrors': numberOfReportingErrors,
                    'numberOfReportingErrors1': numberOfReportingErrors1,
                    'numberOfStaffAdheringToSafety': numberOfStaffAdheringToSafety,
                    'numberOfStaffAudited': numberOfStaffAudited,
                    'adherencetosafety': adherencetosafety,
                    'totalNumberOfMedicationErrors': totalNumberOfMedicationErrors,
                    'totalNumberOfOpportunitiesOfMedicationErrors': totalNumberOfOpportunitiesOfMedicationErrors,
                    'totalNumberOfMedicationErrors': totalNumberOfMedicationErrors,
                    'numberOfTransfusionReactions': numberOfTransfusionReactions,
                    'numberOfUnitsTransfused': numberOfUnitsTransfused,
                    'transfusedreactions': transfusedreactions,
                    'actualDeathInICU': actualDeathInICU,
                    'PredictedDeathsinICU': PredictedDeathsinICU,
                    'morality_ratio_ICU': morality_ratio_ICU,
                    "numberOfPatientsWhoDevelopNewOrWorseningOfPressureUlcer": numberOfPatientsWhoDevelopNewOrWorseningOfPressureUlcer,
                    "totalNoOfRestraintPatientsDays": totalNoOfRestraintPatientsDays,
                    "ulcers_admission": ulcers_admission,
                    'returnsToEmergency':returnsToEmergency,
                    "patientsToEmergency":patientsToEmergency,
                    'return_of_emergency':return_of_emergency,
                    'numberOfUrinaryCatheterAssociatedUTIsInMonth':numberOfUrinaryCatheterAssociatedUTIsInMonth,
                    'numberOfUrinaryCatheterDaysInMonth':numberOfUrinaryCatheterDaysInMonth,
                    'catheterassociated_CDC_NHSN':catheterassociated_CDC_NHSN,
                    'numberOfVentilatorAssociatedPneumonia':numberOfVentilatorAssociatedPneumonia,
                    'numberOfVentilatorDays':numberOfVentilatorDays,
                    'ventilatorassociated_CDC_NHSN':ventilatorassociated_CDC_NHSN,
                    'numberOfCentralLineAssociatedBloodStreamInfectionsInMonth':numberOfCentralLineAssociatedBloodStreamInfectionsInMonth,
                    'numberOfCentralLineDaysInMonth':numberOfCentralLineDaysInMonth,
                    'bloodstrea_CDC_NHSN':bloodstrea_CDC_NHSN,
                    'timeTakenForBloodAndBloodComponents':timeTakenForBloodAndBloodComponents,
                    'totalNoOfBloodAndBloodComponentsCrossMatched':totalNoOfBloodAndBloodComponentsCrossMatched,
                    'available_transfusion':available_transfusion,
                    "numberOfNursingStaff":numberOfNursingStaff,
                    "numberOfBedsOccupied":numberOfBedsOccupied,
                    "patient_ratio_icu":patient_ratio_icu,
                    'timeTakenForDischarge':timeTakenForDischarge,
                    'numberOfPatientsDischarged':numberOfPatientsDischarged,
                    'time_taken_discharge':time_taken_discharge,
                    'NumberofMedicalRecords':NumberofMedicalRecords,
                    'Numberofdischarge':Numberofdischarge,
                    'Numberofdeath':Numberofdeath,
                    'numberofdischargesanddeaths':numberofdischargesanddeaths,
                    'incomplete_improper_constent':incomplete_improper_constent,
                    'waitingTimeForDiagnostics':waitingTimeForDiagnostics,
                    'numberOfPatientsReportedInDiagnostics':numberOfPatientsReportedInDiagnostics,
                    'waiting_time_diagnostics':waiting_time_diagnostics,
                    'timeforconsultation':timeforconsultation,
                    'TotalNumberofop':TotalNumberofop,
                    'time_outpatient_consultation':time_outpatient_consultation,
                    'numberOfNearMissReported':numberOfNearMissReported,
                    'numberOfIncidentsReported':numberOfIncidentsReported,
                    'near_misses':near_misses,
                    'totalNoOfHandoversDoneAppropriately':totalNoOfHandoversDoneAppropriately,
                    'totalNoOfHandoverOpportunities':totalNoOfHandoverOpportunities,
                    'handovers_shift_change':handovers_shift_change,
                    'totalNumberOfPrescriptionInCapitalLetters':totalNumberOfPrescriptionInCapitalLetters,
                    'totalNumberOfPrescriptionSampled':totalNumberOfPrescriptionSampled,
                    'medication_prescription_capitals':medication_prescription_capitals,
                    'numberOfStockOutEmergencyDrugs':numberOfStockOutEmergencyDrugs,
                    'stock_outs_emergency_medications':stock_outs_emergency_medications,
                    'numberOfPatientsDevelopingAdverseDrugReactions':numberOfPatientsDevelopingAdverseDrugReactions,
                    'numberOfInPatients':numberOfInPatients,
                    'adverse_drug_reaction':adverse_drug_reaction,
                    'unplannedReturn':unplannedReturn,
                    "procedureFollowed":procedureFollowed,
                    'unplanned_return_ot':unplanned_return_ot,
                    "procedureFollowed":procedureFollowed,
                    'plannedSurgeries':plannedSurgeries,
                    'percentage_of_surgeries':percentage_of_surgeries,
                    'prophylacticAntibiotic':prophylacticAntibiotic,
                    'plannedSurgeries':plannedSurgeries,
                    'percentage_prophylacticAntibiotic':percentage_prophylacticAntibiotic,
                    'rescheduledCases':rescheduledCases,
                    'plannedSurgeries':plannedSurgeries,
                    're_scheduling_sugeries':re_scheduling_sugeries
                }

                return JsonResponse(response_data, safe=False)
            except Exception as e:
                # Handle database errors
                return JsonResponse({'error': str(e)}, status=500)
        else:
            # Informative error message for missing parameters
            return JsonResponse({'error': 'Please select a year and month'}, status=400)
    else:
        # Error message for disallowed methods
        return JsonResponse({'error': 'Only GET requests are'})
def get_ward_model(ward):
    ward_model_map = {
        'Front Office': FrontOffice,
        'First Floor': FirstFloor,
        'First Suit': FirstSuit,
        'Second Floor': SecondFloor,
        'Second Suit': SecondSuit,
        'Third Floor': ThirdFloor,
        'Lab': Lab,
        'CT': CT,
        'MRI': MRI,
        'X-Ray': Xray,
        'OT': OT,
        'MRD': MRD,
        'MICU': MICU,
        'NICU': NICU,
        'SICU': SICU,
        'Recovery Ward': RecoveryWard,
        'Chemo Ward': ChemoWard,
        'Physiotherapy': Physiotherapy,
        'Dialysis': Dialysis,
        'ER': EmergencyRoom,
    }
    selected_model = ward_model_map.get(ward, None)
    if selected_model:
        return selected_model
    else:
        raise ValueError('Ward type not recognized')
    

from .models import FirstFloorRawData,SecondFloorRawData,SecondSuitRawData    
def get_rawdata_model(ward):
    rawdata_model_map = {
        # 'Recovery Ward Raw Data': RecoveryWardRawData,
        'First Floor Raw Data': FirstFloorRawData,
        'Second Suit Raw Data': SecondSuitRawData,
    }
    selected_rawdata_model = rawdata_model_map.get(ward, None)
    if selected_rawdata_model:
        return selected_rawdata_model
    else:
        raise ValueError('Ward type not recognized')




    
