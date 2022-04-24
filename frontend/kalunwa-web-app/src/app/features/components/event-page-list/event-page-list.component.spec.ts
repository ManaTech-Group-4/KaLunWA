import { HttpClientTestingModule } from '@angular/common/http/testing';
import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EventPageListComponent } from './event-page-list.component';

describe('EventPageListComponent', () => {
  let component: EventPageListComponent;
  let fixture: ComponentFixture<EventPageListComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ EventPageListComponent ],
      imports : [ HttpClientTestingModule ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(EventPageListComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
