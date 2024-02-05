import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.AfterAll;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.util.Random;


class MathUtilsTest {

	@BeforeAll
	static void setUpBeforeClass() throws Exception {
	}

	@AfterAll
	static void tearDownAfterClass() throws Exception {
	}

	@BeforeEach
	void setUp() throws Exception {
	}

	@AfterEach
	void tearDown() throws Exception {
		
	}
	Random random = new Random();
	int i = random.nextInt();
	int j = random.nextInt();
	
    //for addition
	@Test
	void test_add() {
		MathUtils mu = new MathUtils();
		assertEquals(i+j, mu.add(i, j));
		//fail("Not yet implemented");
	}
    //for subtraction
	@Test
	void test_subtract() {
		MathUtils mu = new MathUtils();
		assertEquals(i-j, mu.subtract(i, j));
		//fail("Not yet implemented");
	}
    //for Multiplication
	@Test
	void test_multiply() {
		MathUtils mu = new MathUtils();
		assertEquals(i*j, mu.multiply(i, j));
		//fail("Not yet implemented");
	}
    //for Division
	@Test
	void test_divide() {
		MathUtils mu = new MathUtils();
		 double div=i/j;
		assertEquals(div, mu.divide(i, j));
		//fail("Not yet implemented");
	}
	
	

}
