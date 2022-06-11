import { HttpClientTestingModule } from '@angular/common/http/testing';
import { async, ComponentFixture, inject, TestBed } from '@angular/core/testing';
import { MatDialog, MatDialogModule, MAT_DIALOG_DATA } from '@angular/material/dialog';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { asyncScheduler, of } from 'rxjs';
import { EventsItemsModel } from '../../models/event-items-model';
import { EventspageService } from '../../service/eventspage.service';
import { EventsPageComponent } from './events-page.component';

describe('EventsPageComponent', () => {
  let component: EventsPageComponent;
  let fixture: ComponentFixture<EventsPageComponent>;
  let testBedService : EventspageService;
  let dialogSpy: jasmine.Spy;
  let dialogRefSpyObj = jasmine.createSpyObj({ afterClosed : of({}), close: null })

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ EventsPageComponent ],
      imports : [ MatDialogModule, HttpClientTestingModule, BrowserAnimationsModule],
      providers: [EventspageService]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(EventsPageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
    testBedService = TestBed.get(EventspageService);
    dialogSpy = spyOn(TestBed.get(MatDialog), 'open').and.returnValue(dialogRefSpyObj);
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });


  it('Service injected via inject() and TestBed.get() should be the same instance (EventpageService)',
    inject([EventspageService], (injectService: EventspageService) => {
      expect(injectService).toBe(testBedService);
  }));


  it("should call openDialog and get the list of events according to fiter", async(() => {
    const response: EventsItemsModel[] = [];

    spyOn(component, 'openDialog');

    component.openDialog();

    fixture.detectChanges();
    let result= [] as EventsItemsModel[];
    component.eventDisplay$.subscribe(events =>{result = events;
    })
    expect(result).toEqual(response);
  }));

});
