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
});
