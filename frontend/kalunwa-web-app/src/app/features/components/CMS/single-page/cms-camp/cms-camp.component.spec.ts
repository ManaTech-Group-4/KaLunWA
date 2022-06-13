import { ComponentFixture, TestBed } from '@angular/core/testing';
import { HttpClientTestingModule } from '@angular/common/http/testing';
import { ReactiveFormsModule, FormsModule } from '@angular/forms';
import { RouterTestingModule } from "@angular/router/testing";
import { CmsCampComponent } from './cms-camp.component';

describe('CmsCampComponent', () => {
  let component: CmsCampComponent;
  let fixture: ComponentFixture<CmsCampComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CmsCampComponent ],
      imports:[
        HttpClientTestingModule,
        ReactiveFormsModule,
        FormsModule,
        RouterTestingModule,]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(CmsCampComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
