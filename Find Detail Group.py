"""Find all location of selected detail group"""
__author__='NguyenKhanhTien - khtien0107@gmail.com'
from Autodesk.Revit.DB import FilteredElementCollector, BuiltInCategory, Transaction, ViewSheet
from rpw import ui
doc = __revit__.ActiveUIDocument.Document
detailgroups_collector=FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_IOSDetailGroups)\
                    .WhereElementIsNotElementType()\
                    .ToElements()

viewsheet = FilteredElementCollector(doc).OfClass(ViewSheet)\
                    .WhereElementIsNotElementType()\
                    .ToElements()

detailgroups = []
selection = ui.Selection()
name = selection[0].Name
count = 0
for dg in detailgroups_collector:
	if dg.Name == name:
		detailgroups.append(dg)
		count +=1

divide = "**********************************************************************************************************************"
divide2 = "--------------------------"
print("GROUP NAME: "+ name + '\n'+"TOTAL: " + str(count))
print(divide)
print("LOCATION:")

for detail in detailgroups:
	e=doc.GetElement(detail.OwnerViewId)
	print e.Title
	for vs in viewsheet:
		for eid in vs.GetAllPlacedViews():
			ev=doc.GetElement(eid)
			if ev.Id == e.Id:
				print ("Sheet " + vs.SheetNumber + ": " + vs.Name)
				break
	print (divide2)
	