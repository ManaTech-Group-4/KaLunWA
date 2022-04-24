import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { By } from '@angular/platform-browser';

import { OrgStructureComponent } from './org-structure.component';

describe('OrgStructureComponent', () => {
  let component: OrgStructureComponent;
  let fixture: ComponentFixture<OrgStructureComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ OrgStructureComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(OrgStructureComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
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
});
