import { Overlay } from '@angular/cdk/overlay';
import { HttpClientTestingModule } from '@angular/common/http/testing';
import { async, ComponentFixture, inject, TestBed } from '@angular/core/testing';
import {MatDialog, MatDialogModule} from '@angular/material/dialog';
import { By } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { Observable, of } from 'rxjs';
import { MembersDialogModel } from '../../models/members-dialog-model';
import { OrgService } from '../../service/org.service';

import { OrgStructureComponent } from './org-structure.component';



describe('OrgStructureComponent', () => {
  let component: OrgStructureComponent;
  let fixture: ComponentFixture<OrgStructureComponent>;
  let testBedService : OrgService;
  let dialogSpy: jasmine.Spy;
  let dialogRefSpyObj = jasmine.createSpyObj({ afterClosed : of({}), close: null })

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [MatDialogModule, HttpClientTestingModule, BrowserAnimationsModule],
      declarations: [ OrgStructureComponent ],
      providers: [OrgService]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(OrgStructureComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
    testBedService = TestBed.get(OrgService);
    dialogSpy = spyOn(TestBed.get(MatDialog), 'open').and.returnValue(dialogRefSpyObj);
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  it('should click Camps Button', async(() => {
    fixture.detectChanges();
    let buttonElement = fixture.debugElement.query(By.css('.camp-button'));

    buttonElement.triggerEventHandler('click', null);
    fixture.detectChanges();

    fixture.whenStable().then(() => {
      expect(component.showBaybayon).toBeTruthy();
    });
  }));


  it('should click BoT Button', async(() => {
    fixture.detectChanges();
    let buttonElement = fixture.debugElement.query(By.css('.bot-button'));

    buttonElement.triggerEventHandler('click', null);
    fixture.detectChanges();

    fixture.whenStable().then(() => {
      expect(component.showBoT).toBeTruthy();
    });
  }));

  it('changes the value of BoT(if true) to false after clicking to Baybayon', () =>{
    component.showBoT = true;
    component.clickBaybayon();

    expect(component.showBoT).toBeFalse();
  });

  it('changes the value of BoT(if true) to false after clicking to Suba', () =>{
    component.showBoT = true;
    component.clickSuba();

    expect(component.showBoT).toBeFalse();
  });

  it('changes the value of BoT(if true) to false after clicking to Lasang', () =>{
    component.showBoT = true;
    component.clickLasang();

    expect(component.showBoT).toBeFalse();
  });

  it('changes the value of BoT(if true) to false after clicking to Zero Waste', () =>{
    component.showBoT = true;
    component.clickZW();

    expect(component.showBoT).toBeFalse();
  });

  it('Service injected via inject() and TestBed.get() should be the same instance (OrgService)',
    inject([OrgService], (injectService: OrgService) => {
      expect(injectService).toBe(testBedService);
  }));

  it("should call openDialog and get the list of events according to fiter", async(() => {
    const response: MembersDialogModel[] = [];

    spyOn(component, 'openDialog');

    component.openDialog(component.directors$);

    fixture.detectChanges();
    let result= [] as MembersDialogModel[];
    component.directors$.subscribe(events =>{result = events;
    })
    expect(result).toEqual(response);
  }));

  it("filter an observable with position", async(() => {
    const response: Observable<MembersDialogModel[]> = of([
      {id: 1,
      first_name: "Jairus",
      image: {image: "http://127.0.0.1:8000/media/images/content/event.jpg"},
      last_name: "de la Cruz",
      position: "Director",
      quote: "advocacy"
      },
      {id: 2,
      first_name: "Juan",
      image: {image: "http://127.0.0.1:8000/media/images/content/event.jpg"},
      last_name: "Chiu",
      position: "Director",
      quote: "advocacy"
      },
    ]);

    const mock: Observable<MembersDialogModel[]>  = of([
      {id: 1,
      first_name: "Jairus",
      image: {image: "http://127.0.0.1:8000/media/images/content/event.jpg"},
      last_name: "de la Cruz",
      position: "Director",
      quote: "advocacy"
      },
      {id: 2,
      first_name: "Juan",
      image: {image: "http://127.0.0.1:8000/media/images/content/event.jpg"},
      last_name: "Chiu",
      position: "Director",
      quote: "advocacy"
      },
      {id: 3,
      first_name: "Jairus",
      image: {image: "http://127.0.0.1:8000/media/images/content/event.jpg"},
      last_name: "Chiu",
      position: "President",
      quote: "advocacy"
      },
      {id: 4,
      first_name: "Juan",
      image: {image: "http://127.0.0.1:8000/media/images/content/event.jpg"},
      last_name: "Tamad",
      position: "Estambay",
      quote: "advocacy"
      }
    ]);

    component.getLeadersList("Director",mock);
    expect(mock.subscribe()).toEqual(response.subscribe());
  }));


});
