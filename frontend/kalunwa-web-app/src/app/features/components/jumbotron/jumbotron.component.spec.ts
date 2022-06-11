import { ComponentFixture, inject, TestBed } from '@angular/core/testing';
import { JumbotronComponent } from './jumbotron.component';
import { HttpClientTestingModule} from '@angular/common/http/testing';
import { HomepageService } from '../../service/homepage.service';

describe('JumbotronComponent', () => {
  let component: JumbotronComponent;
  let fixture: ComponentFixture<JumbotronComponent>;
  let testBedService : HomepageService;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ JumbotronComponent ],
      imports: [ HttpClientTestingModule ],
      providers: [HomepageService]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(JumbotronComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();

    testBedService = TestBed.get(HomepageService);
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  it('Service injected via inject() and TestBed.get() should be the same instance (HomepageService)',
    inject([HomepageService], (injectService: HomepageService) => {
      expect(injectService).toBe(testBedService);
  }));

});
